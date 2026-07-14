# Installation & Setup Guide

This guide covers setting up, running, packaging, and deploying the **ROV Remote Controller**.

---

## 1. Running the Server from Source

To run the Python server directly from the source code:

### Step 1: Install Python
Ensure you have **Python 3.8** or higher installed. You can check your version by running:
```bash
python --version
```

### Step 2: Clone the Project
Clone this repository to your host computer:
```bash
git clone https://github.com/aryan/Controller.git
cd Controller
```

### Step 3: Set Up a Virtual Environment (Recommended)
Creating a virtual environment isolates the dependencies of this project:

*   **Windows**:
    ```powershell
    python -m venv venv
    .\venv\Scripts\Activate.ps1
    ```
*   **macOS / Linux**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

### Step 4: Install Dependencies
Install all required libraries using the package manager `pip`:
```bash
pip install -r requirements.txt
```

### Step 5: Start the Host Server
Execute the server script:
```bash
python src/server.py
```
This will launch a GUI popup displaying the QR code and print connection details to your terminal.

---

## 2. Packaging the Server into an Executable (EXE)

To bundle the server into a standalone executable that runs without requiring Python to be installed on the host PC:

### Step 1: Install PyInstaller
Ensure PyInstaller is installed in your python environment:
```bash
pip install pyinstaller
```

### Step 2: Build the Executable
Run the PyInstaller compiler targeting `src/server.py`. We need to ensure that the static client files are bundled with the executable so the server can serve them:

*   **Windows (PowerShell)**:
    ```powershell
    pyinstaller --onefile --noconsole --add-data "src/client/index.html;src/client" src/server.py
    ```
*   **macOS / Linux**:
    ```bash
    pyinstaller --onefile --noconsole --add-data "src/client/index.html:src/client" src/server.py
    ```

*Note on flags:*
*   `--onefile`: Packages the application into a single self-contained executable file.
*   `--noconsole`: Hides the console command prompt window when the server runs. (Remove this flag during debugging to see log outputs).
*   `--add-data`: Bundles the `index.html` file into the relative virtual directory of the packed binary.

### Step 3: Find the Executable
Once packaging completes:
1.  Navigate to the `/dist` directory in the project root.
2.  Run `server.exe` to boot the server.

---

## 3. Deploying the Mobile Clients

You can connect to the server using either the Native Android App or the Web-Based Controller.

### Option A: Sideloading the Android APK
The project contains pre-compiled Android release packages in the `/releases` folder.

1.  Extract the ZIP file `releases/ROV_V_2.4.5.zip` to locate `rov_1.3.apk`.
2.  Transfer the `rov_1.3.apk` file to your Android phone.
3.  Open the APK file on your device.
4.  If prompted with a warning stating "Install blocked: Unverified Developer," grant the system permission to install from unknown sources.
5.  Install and launch the **ROV** app.
6.  Ensure your phone's Wi-Fi is turned on and connected to the same network as your PC.
7.  Tap **Scan** inside the app and scan the QR code displayed on your PC monitor.

### Option B: Zero-Installation Web Controller
No app installation is required to use this option!

1.  Make sure your mobile phone is connected to the same local Wi-Fi network as the PC.
2.  Open any browser on your phone (Chrome, Safari, Firefox).
3.  Type in the Web Client URL printed in your PC's terminal when starting the server. For example:
    `http://192.168.1.10:8765`
4.  The browser will load the touch-keyboard interface and automatically link to the controller server.
5.  *Tip*: Add the page to your phone's home screen (using the browser's "Add to Home Screen" option) to use it as a fullscreen standalone web-app!
