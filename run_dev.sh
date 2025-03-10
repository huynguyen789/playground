#!/bin/bash
# Run the MCP server in development mode

# Activate the virtual environment
source .venv/bin/activate

echo "Starting MCP Server in development mode..."
mcp dev calculator_server.py 