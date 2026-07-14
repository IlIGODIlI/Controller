# Frequently Asked Questions (FAQ)

This page lists common troubleshooting steps and questions about the **ROV Remote Controller**.

---

## 📶 Connection & Networking

### Q: Why is my phone unable to connect to the PC server?
Verify the following network parameters:
1.  **Same Wi-Fi Network**: Check that both the phone and PC are connected to the exact same Wi-Fi router.
2.  **VPN Status**: Turn off any active VPN, proxy, or corporate firewall tunnel on both devices.
3.  **Firewall Obstruction**: Your PC's firewall might be blocking port `8765`. Refer to the [Firewall Guide](CONFIGURATION.md#3-network---firewall-configuration) to whitelist python/server executable.
4.  **Local IP Address**: If your local IP address changed, scan the QR code again to update the client's saved connection profile.

### Q: What does "AP Isolation" mean and why does it break the connection?
Access Point (AP) Isolation is a security setting on some Wi-Fi routers (especially public hot-spots or guest networks) that prevents connected wireless devices from pinging or talking to each other. You must disable AP Isolation in your router settings, or run a mobile hotspot from your phone and connect your PC to it.

---

## ⚡ Latency & Gameplay

### Q: How can I reduce touch latency?
WebSocket latency is highly dependent on your local wireless signal.
*   Move closer to your Wi-Fi router.
*   Use a **5 GHz** Wi-Fi band instead of a 2.4 GHz band, as it offers much higher throughput and lower interference.
*   Close high-bandwidth background apps on your phone or PC (torrents, video streaming, downloads).
*   Alternatively, turn on your Android phone's **Wi-Fi Hotspot**, connect your PC to the hotspot network, and run the server. This bypasses the router entirely, resulting in sub-millisecond response times!

### Q: Why do keys get stuck occasionally?
If a key gets "stuck" in the down position on your PC:
*   This can occur if a network dropout happens exactly when you release a key on the phone, preventing the `up:<key>` message from arriving.
*   Simply tap/press the stuck key again on the controller keyboard. This sends a new down/up sequence, resetting the state of that key in PyAutoGUI.
*   In the modernized Web Client (`src/client/index.html`), we have added safety event handlers (`mouseleave`, `touchcancel`) to ensure mouse drags and interrupted touch sweeps release the key automatically.

---

## 🛡️ Warnings & Security

### Q: Why does my browser or antivirus flag the mobile app or server?
*   **Android APK**: Sideloading any application that is not distributed via the Google Play Store prompts a security alert. This is standard behavior. The APK does not request any dangerous system permissions (only Internet and Camera, which are needed to connect and scan the QR code).
*   **Windows server.exe**: Executables compiled with PyInstaller are sometimes flagged as false positives by antivirus scanners. This is because PyInstaller bundles all files into a self-extracting archive, which resembles malware structure to basic signature scanners. The source code is 100% open-source and reviewable in [src/server.py](../src/server.py). You can avoid warnings by running the server directly from source code using standard Python.
*   **Keystroke simulation**: Security software may flag python's `pyautogui` because it can inject system-wide keyboard events. This is the core functionality of ROV, and is fully safe when used in your local network.
