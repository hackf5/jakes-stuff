#!/usr/bin/env bash
# Poker Game Launcher Script

echo "🎰 Welcome to Command Line Poker! 🎰"
echo "======================================"
echo ""

# Check if poetry is installed
if ! command -v poetry &> /dev/null; then
    echo "❌ Poetry is not installed. Please install poetry first."
    echo "Visit: https://python-poetry.org/docs/#installation"
    exit 1
fi

# Check if we're in the right directory
if [ ! -f "pyproject.toml" ]; then
    echo "❌ Please run this script from the poker directory"
    exit 1
fi

# Install dependencies if needed
if [ ! -d ".venv" ] && [ ! -f "poetry.lock" ]; then
    echo "📦 Installing dependencies..."
    poetry install
fi

# Run the game
echo "🚀 Starting poker game..."
echo ""
poetry run poker
