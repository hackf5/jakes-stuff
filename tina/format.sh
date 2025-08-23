#!/bin/bash

# Format and lint the Tina project

echo "🔧 Running isort to sort imports..."
poetry run isort tina/

echo "🎨 Running black to format code..."
poetry run black tina/

echo "🔍 Running flake8 to check for style issues..."
poetry run flake8 tina/

echo "🏷️  Running mypy for type checking..."
poetry run mypy tina/

echo "✅ Linting and formatting complete!"
