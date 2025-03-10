#!/bin/bash
# Run the calculator server in development mode

# Activate the virtual environment
source .venv/bin/activate

echo "Starting Calculator MCP Server in development mode..."
mcp dev calculator_server.py 