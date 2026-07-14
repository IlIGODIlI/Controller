# Security Policy

We take the security of the **ROV Remote Controller** seriously. This document outlines how to report vulnerabilities and describes which versions are actively supported.

---

## ⚠️ Important Deployment Warning

> [!WARNING]
> **ROV communicates unencrypted (plain HTTP and raw WebSockets) over your local area network (LAN).** It does not implement Transport Layer Security (TLS/WSS) or authentication mechanisms.
>
> *   **Do NOT run this server on public or untrusted networks** (such as coffee shop Wi-Fi or public hotspots).
> *   Anyone on the same network who discovers the server port could send simulated keystroke events to control your host PC.
> *   Keep your QR code private; sharing it exposes your local IP address.

---

## Supported Versions

Only the latest major release receives active security patches.

| Version | Supported |
| :--- | :--- |
| 3.x.x (Modernized) |  Yes |
| 2.x.x | ❌ No |
| 1.x.x | ❌ No |

---

## Reporting a Vulnerability

If you discover a security vulnerability in this project:

1.  **Do NOT open a public GitHub issue.** Doing so discloses the vulnerability publicly before a fix is available.
2.  Send an email to the maintainer at `aryan@example.com` describing the issue in detail.
3.  Include steps to reproduce, potential impact, and details of your testing environment.

We will acknowledge receipt of your report within 48 hours and work to provide a resolution within 14 days. Once resolved, we will publish a security advisory and credit you for the discovery.
