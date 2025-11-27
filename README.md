# PyMidnight 🐍

A minimal Python SDK skeleton and CLI for Midnight (mock mode).

## 🚀 Overview

Welcome to PyMidnight! This project provides a Python Software Development Kit (SDK) and a Command-Line Interface (CLI) designed to interact with the Midnight service.

It is built using modern Python tools to ensure a great developer experience and a robust, user-friendly CLI. Currently, it operates in a **mock mode**, allowing for development and testing without a live connection to the Midnight service. This makes it an ideal starting point for building out a full-featured client.

## 🤔 Why PyMidnight?

In the world of services and APIs, having a dedicated client library simplifies integration, reduces boilerplate code, and provides a more intuitive interface than raw HTTP requests. PyMidnight aims to be that client for the Midnight service.

*   **For End-Users**: A powerful and scriptable CLI to manage Midnight resources directly from the terminal.
*   **For Developers**: A clean and modern Python SDK to integrate Midnight into other Python applications.
*   **For Contributors**: A well-structured project using best-in-class tools, making it easy to get started and contribute.

## ✨ Features

*   **Modern CLI**: A rich and easy-to-use command-line interface built with [Typer](https://typer.tiangolo.com/) and [Rich](https://github.com/Textualize/rich) for beautiful formatting and intuitive commands.
*   **HTTP Communication**: Uses the popular [Requests](https://requests.readthedocs.io/en/latest/) library for simple and reliable communication with web services.
*   **Dependency Management**: Project dependencies are managed with [Poetry](https://python-poetry.org/) for reproducible and deterministic builds.
*   **Testing Framework**: Comes pre-configured with [Pytest](https://docs.pytest.org/) for writing simple and scalable tests.
*   **Extensible**: Designed as a skeleton, it's easy to add new commands, SDK methods, and features.

## 📂 File Structure

Here is a brief overview of the key files in this project:

*   `poetry.lock`: An auto-generated file by Poetry that locks the project's dependencies to specific versions. This ensures that everyone working on the project uses the exact same package versions.
*   `pyproject.toml`: The core Poetry configuration file where project metadata, dependencies, and tool configurations are declared.
*   `README.md`: This file, providing documentation and instructions for the project.
*   `pymidnight/`: The main source code directory for the Python package.
    *   `cli.py`: (Assumed) The entry point for the Typer-based command-line application.

## ⚙️ Setup and Installation

To get started with PyMidnight, you'll need Python and Poetry installed on your system.

1.  **Clone the repository (if applicable):**
    ```bash
    git clone https://your-repository-url/pymidnight.git
    cd pyMidnight
    ```

2.  **Install Dependencies:**
    Use Poetry to install all the required dependencies from the `poetry.lock` file. This creates a virtual environment and installs everything needed to run and develop the project.
    ```powershell
    poetry install
    ```

3.  **Activate the Virtual Environment:**
    To use the installed packages and run the CLI, activate the Poetry-managed virtual environment.
    ```powershell
    poetry shell
    ```

## 🎮 Usage

The project is configured with a script entry point, allowing you to call it directly from your terminal once installed.

### Command-Line Interface (CLI)

The CLI is built with Typer, which provides automatic help generation. To see all available commands and options:

```bash
pymidnight --help
```

While the project is a skeleton, here is a hypothetical example of how you might interact with it once features are added:

```bash
# Example: Get the status of a resource
pymidnight get status --resource-id "abc-123"

# Example: Create a new item with a description
pymidnight create item --name "My New Item" --description "This is a test item."
```

### Software Development Kit (SDK)

You can also use the `pymidnight` package as a library in your own Python projects.

```python
# main.py
from pymidnight import sdk

def main():
    # Create a client (authentication might be handled here)
    client = sdk.MidnightClient()

    # Use the client to interact with the service
    status = client.get_status(resource_id="abc-123")
    print(f"Resource status: {status}")

if __name__ == "__main__":
    main()
```

## 🛠️ Development

We welcome contributions! This project uses `pytest` for testing.

To run the test suite:

```bash
# Make sure you are in the poetry shell
pytest
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## 📧 Contact

Huy Anh - golem25012001@gmail.com

Project Link: https://github.com/ADA-BAMBOO/pymidnight.git

