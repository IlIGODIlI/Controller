# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [3.0.0] - 2026-07-14

This release represents a complete architectural modernization and structural overhaul of the repository.

### Added
*   **Unified HTTP/WS Server**: The python backend now acts as a concurrent HTTP static file server on port `8765`, serving the web client HTML page directly to web browsers.
*   **Modernized Web Client**: Rewrote `src/client/index.html` with a premium glassmorphic UI, Inter/Outfit typography, responsive keyboard layout, micro-animations, and WebSocket connectivity (replacing legacy fetch loops).
*   **Command Line Arguments**: Added `--port`, `--host`, and `--no-qr` flags to `src/server.py` using `argparse`.
*   **Configuration Files**: Added `.gitignore`, `requirements.txt`, and standard `pyproject.toml` configuration files.
*   **Comprehensive Documentation**: Created `/docs` directory housing `ARCHITECTURE.md`, `INSTALLATION.md`, `CONFIGURATION.md`, `FAQ.md`, and `CONTRIBUTING.md`.
*   **Community Files**: Added `CODE_OF_CONDUCT.md`, `SECURITY.md`, and issue/PR templates.
*   **Branding Assets**: Created professional logo and widescreen banner assets under `/assets`.
*   **CI Validation**: Added GitHub Actions linting workflow `.github/workflows/lint.yml`.

### Changed
*   **Repository Restructuring**: Reorganized the flat repository layout into clean directories (`src/`, `docs/`, `releases/`, `assets/`).
*   **Refactoring**: Refactored Python and HTML code to conform to PEP-8 standards.
*   **Relocation**: Moved pre-built zips containing executables and APKs into `/releases`.

### Removed
*   Deprecated flat files `HOW_TO_USE` and `Personal_Log` (their contents were fully integrated into the new markdown documentation).

---

## [2.4.5] - 2026-03-10

### Added
*   Bundled `rov_1.3.apk` and `server.exe` in `ROV_V_2.4.5.zip`.
*   Added auto-reconnection mechanics in the mobile APK.
*   Implemented persistent storage of the last scanned system IP to auto-connect on subsequent app launches.

### Fixed
*   Reduced communication latency.

---

## [1.8.2] - 2025-11-05

### Added
*   Initial experimental release bundled in `ROV_V_1.8.2.zip`.
*   Basic WebSocket communication protocol matching `down:key` and `up:key` commands.
*   PyAutoGUI input simulation engine.
*   Automatic local IP resolution and QR code popup display.
