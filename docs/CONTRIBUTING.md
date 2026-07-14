# Contributing Guidelines

Thank you for your interest in contributing to **ROV**! We welcome contributions to improve performance, add layout features, or expand documentation.

---

## 1. Code of Conduct

By participating in this project, you agree to abide by our [Code of Conduct](../CODE_OF_CONDUCT.md). Please report any unacceptable behavior to the repository owner.

---

## 2. Workspace Setup

To set up a local development workspace:

1.  Fork the repository on GitHub.
2.  Clone your fork locally:
    ```bash
    git clone https://github.com/<YOUR_USERNAME>/Controller.git
    cd Controller
    ```
3.  Set up a virtual environment and install the development dependencies:
    ```bash
    python -m venv venv
    # Activate virtual environment
    # Windows:
    .\venv\Scripts\Activate.ps1
    # Unix:
    source venv/bin/activate
    
    # Install dependencies
    pip install -r requirements.txt
    pip install black isort flake8
    ```

---

## 3. Style & Code Quality

To maintain a clean and professional codebase, we enforce standard formatting rules.

### Python Style Rules
*   **PEP 8 Compliance**: Follow standard Python conventions.
*   **Formatting**: We use **Black** for auto-formatting and **isort** for sorting imports.
    *   To run Black:
        ```bash
        black src/
        ```
    *   To run isort:
        ```bash
        isort src/
        ```
*   **Linting**: We check code using `flake8` to catch syntactic errors, unused imports, or style violations:
    ```bash
    flake8 src/ --max-line-length=88 --exclude=venv
    ```

### HTML/CSS Style Rules
*   Use semantic HTML5 tags where possible.
*   Maintain clean, indented CSS with custom variables for color schemes.
*   Avoid inline Javascript scripts; bind event handlers using the script block or selectors.

---

## 4. Verification Check

Before submitting a Pull Request, always verify that your code compiles and has no syntax errors:

```bash
# Check python syntax
python -m py_compile src/server.py
```

We also recommend testing the client-server connection manually by launching the server and opening `http://localhost:8765` in a browser.

---

## 5. Submitting a Pull Request

When your changes are ready:

1.  Create a descriptive branch for your feature or fix:
    ```bash
    git checkout -b feature/add-gamepad-keys
    ```
2.  Commit your changes with clear, semantic commit messages (e.g. `feat: add ESC key to layout`, `fix: handle connection reset in server`).
3.  Push your branch to your GitHub fork:
    ```bash
    git push origin feature/add-gamepad-keys
    ```
4.  Open a Pull Request against the `main` branch of the original repository.
5.  Ensure that the automated PR checklist in our [Pull Request Template](../.github/PULL_REQUEST_TEMPLATE.md) is filled out completely.
