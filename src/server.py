import argparse
import asyncio
import logging
import os
import socket
import sys
import pyautogui
import qrcode
import websockets
from websockets.http11 import Response
from websockets.datastructures import Headers

# Configure PyAutoGUI settings
pyautogui.PAUSE = 0
pyautogui.FAILSAFE = False

# Setup logging configuration (using ASCII characters for Windows compatibility)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("ROVServer")

def get_local_ip():
    """Detects the host's local IP address by attempting an outgoing connection."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Does not send actual packets, just establishes local socket path
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip

def make_process_request(client_html_path):
    """Factory to create a process_request handler with access to client_html_path."""
    async def process_request(connection, request):
        # If the client requested a WebSocket upgrade, let the default handshake handle it
        if "upgrade" in request.headers:
            return None
        
        path = request.path
        # Serve the web client for root or index.html requests
        if path in ("/", "/index.html", "/client"):
            if not os.path.exists(client_html_path):
                err_msg = f"Client interface file not found at {client_html_path}.".encode("utf-8")
                return Response(
                    status_code=404,
                    reason_phrase="Not Found",
                    headers=Headers([
                        ("Content-Type", "text/plain; charset=utf-8"),
                        ("Content-Length", str(len(err_msg))),
                        ("Connection", "close")
                    ]),
                    body=err_msg
                )
            try:
                with open(client_html_path, "r", encoding="utf-8") as f:
                    body = f.read().encode("utf-8")
                return Response(
                    status_code=200,
                    reason_phrase="OK",
                    headers=Headers([
                        ("Content-Type", "text/html; charset=utf-8"),
                        ("Content-Length", str(len(body))),
                        ("Connection", "close")
                    ]),
                    body=body
                )
            except Exception as e:
                err_msg = f"Error reading client interface: {str(e)}".encode("utf-8")
                return Response(
                    status_code=500,
                    reason_phrase="Internal Server Error",
                    headers=Headers([
                        ("Content-Type", "text/plain; charset=utf-8"),
                        ("Content-Length", str(len(err_msg))),
                        ("Connection", "close")
                    ]),
                    body=err_msg
                )
        
        # 404 Not Found for any other HTTP requests
        body = b"Not Found"
        return Response(
            status_code=404,
            reason_phrase="Not Found",
            headers=Headers([
                ("Content-Type", "text/plain; charset=utf-8"),
                ("Content-Length", str(len(body))),
                ("Connection", "close")
            ]),
            body=body
        )
    return process_request

async def handler(websocket):
    """Handles WebSocket controller sessions."""
    client_address = websocket.remote_address
    logger.info(f"Phone connected from {client_address[0]}:{client_address[1]}")
    try:
        async for message in websocket:
            # Skip keep-alive ping messages
            if message == "ping":
                continue
            
            # Message formatting verification (command:key)
            if ":" not in message:
                logger.warning(f"Malformed message received: {message}")
                continue
            
            command, key = message.split(":", 1)
            
            if command == "down":
                logger.debug(f"Key Down: {key}")
                pyautogui.keyDown(key)
            elif command == "up":
                logger.debug(f"Key Up: {key}")
                pyautogui.keyUp(key)
            else:
                logger.warning(f"Unknown command: {command} for key {key}")
    except Exception as e:
        logger.error(f"Connection error with client {client_address}: {e}")
    finally:
        logger.info(f"Phone disconnected from {client_address[0]}:{client_address[1]}")

async def main():
    parser = argparse.ArgumentParser(description="ROV WebSocket Remote Controller Server")
    parser.add_argument("--host", default="0.0.0.0", help="Host interface to bind to (default: 0.0.0.0)")
    parser.add_argument("--port", type=int, default=8765, help="Port to listen on (default: 8765)")
    parser.add_argument("--no-qr", action="store_true", help="Disable launching the QR code popup image window")
    args = parser.parse_args()

    local_ip = get_local_ip()
    ws_url = f"ws://{local_ip}:{args.port}"
    http_url = f"http://{local_ip}:{args.port}"

    logger.info("WebSocket controller server initializing...")
    logger.info(f"Listening on: {args.host}:{args.port}")
    logger.info(f"WebSocket Controller URL: {ws_url}")
    logger.info(f"Web Client URL:           {http_url}")

    # Generate and display QR Code
    if not args.no_qr:
        logger.info("Generating QR code...")
        try:
            qr = qrcode.make(ws_url)
            qr.show()
            logger.info("QR code window opened. Scan with the mobile app or browser.")
        except Exception as e:
            logger.error(f"Failed to generate/display QR code: {e}")
            logger.info("Proceeding server run without QR popup.")

    # Locate the client index.html path relative to this script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    client_html_path = os.path.join(current_dir, "client", "index.html")

    # Run the combined HTTP and WebSocket server
    async with websockets.serve(
        handler,
        args.host,
        args.port,
        ping_interval=20,
        ping_timeout=30,
        process_request=make_process_request(client_html_path)
    ):
        await asyncio.Future()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Server stopped by user. Goodbye!")