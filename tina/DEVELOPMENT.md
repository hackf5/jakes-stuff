# Development Tools

This project includes linting and formatting tools to maintain code quality.

## Available Tools

- **Black**: Code formatter that enforces consistent style
- **isort**: Import sorter that organizes imports
- **flake8**: Linter that checks for style guide violations
- **mypy**: Static type checker for Python

## Usage

### Quick Format and Lint

Run the format script to format and check all code:

```bash
./format.sh
```

### Individual Tool Commands

Format code with Black:
```bash
poetry run black tina/
```

Sort imports with isort:
```bash
poetry run isort tina/
```

Check style with flake8:
```bash
poetry run flake8 tina/
```

Type check with mypy:
```bash
poetry run mypy tina/
```

## Configuration

- **Black**: Configured in `pyproject.toml` with 88 character line length
- **isort**: Configured to be compatible with Black in `pyproject.toml`
- **flake8**: Configured in `.flake8` file with Black-compatible settings
- **mypy**: Configured in `pyproject.toml` with strict type checking

## Pre-commit Hook (Optional)

You can set up a git pre-commit hook to automatically run formatting:

```bash
# Create pre-commit hook
cat > .git/hooks/pre-commit << 'EOF'
#!/bin/bash
cd "$(git rev-parse --show-toplevel)/tina"
./format.sh
if [ $? -ne 0 ]; then
    echo "Linting failed. Please fix the issues and try again."
    exit 1
fi
EOF

chmod +x .git/hooks/pre-commit
```
