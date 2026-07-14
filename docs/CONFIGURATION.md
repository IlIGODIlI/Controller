# Configuration & Customization Guide

This document describes how to configure network parameters, command-line arguments, and keyboard bindings in the **ROV Remote Controller**.

---

## 1. Command-Line Arguments

When launching `src/server.py` from source, you can customize its behavior using flags.

### Usage
```bash
python src/server.py [options]
```

### Options List

| Argument | Description | Default Value | Example |
| :--- | :--- | :--- | :--- |
| `--host` | The network interface the server will bind to. | `0.0.0.0` (binds to all interfaces) | `--host 192.168.1.15` |
| `--port` | The TCP port used for HTTP and WebSocket streams. | `8765` | `--port 9000` |
| `--no-qr` | Skips generating and displaying the QR code window. Useful for headless servers or automated testing. | `False` (will show QR code popup) | `--no-qr` |

---

## 2. Keyboard Key Bindings

The buttons in `src/client/index.html` send strings that map directly to the keys simulated by the PyAutoGUI engine on the host OS.

### Supported Keys
The following table shows how key codes correspond between the client buttons and PyAutoGUI mapping:

| Client Button Label | Sent Key Value | PyAutoGUI Action |
| :--- | :--- | :--- |
| `Q` - `Z` | `'q'` - `'z'` | Normal lowercase letter keys |
| `1` - `0` | `'1'` - `'0'` | Numeric keys |
| `SHIFT` | `'shift'` | Simulates holding/releasing physical Shift |
| `SPACE` | `'space'` | Simulates spacebar |
| `ENTER` | `'enter'` | Simulates Return / Enter |
| `⌫` | `'backspace'` | Simulates Backspace |
| `←` `↓` `↑` `→` | `'left'`, `'down'`, `'up'`, `'right'` | Keyboard directional arrows |

### Modifying Key Mappings
If you want to add new keys or change mappings:
1.  Open `src/client/index.html` in an editor.
2.  Locate the key layout grids:
    ```html
    <div class="key" data-key="w">W</div>
    ```
3.  Modify the `data-key` attribute to match any of the valid PyAutoGUI keys. For example, to map a key to escape, use:
    ```html
    <div class="key key-special" data-key="esc">ESC</div>
    ```
    *Refer to the [PyAutoGUI documentation](https://pyautogui.readthedocs.io/en/latest/keyboard.html#keyboard-keys) for a complete list of valid key names (e.g. `esc`, `ctrl`, `alt`, `f1`-`f12`).*

---

## 3. Network & Firewall Configuration

Because ROV streams input over your local network, your host operating system's firewall may block incoming client connection attempts.

### Windows Firewall Configuration
If your mobile client fails to connect or scan times out:
1.  Open the **Control Panel** on Windows.
2.  Navigate to **System and Security** &rarr; **Windows Defender Firewall** &rarr; **Allowed Apps**.
3.  Click **Change Settings**.
4.  Ensure that **python.exe** (or your compiled `server.exe`) is allowed to communicate on **Private** networks.
5.  If it is not listed, click **Allow another app...** and browse to the path of your python interpreter or packaged executable.

### Same-Network Restriction
*   The host PC and the mobile device **must be connected to the same subnet/Wi-Fi router**.
*   Verify that your router does not have **AP Isolation / Client Isolation** enabled. This feature prevents wireless clients from communicating with each other.
*   Make sure any VPN software is disabled on both devices, as VPN tunnels route traffic away from the local subnet.
