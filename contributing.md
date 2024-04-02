# Contributing Guidelines

## Using Linters

In this project, we use the following linters to maintain code quality:

- **ruff**: A custom linting tool for enforcing code style and best practices in our Python code.
- **mypy**: A static type checker for Python.

### ruff
Ruff is our custom linting tool that ensures consistency and adherence to coding standards in our Python codebase.

```bash
# Install Ruff using pip
pip install ruff

# Navigate to your project directory
cd /path/to/your/project

# Run Ruff to check your Python files
ruff check your_file.py

### mypy
# Install Mypy using pip
pip install mypy

# Navigate to your project directory
cd /path/to/your/project

# Run Mypy on your Python files
mypy your_file.py
