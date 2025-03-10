#!/bin/bash
# File: run_calculator_mcp.sh
# Wrapper script for running the calculator MCP server in Cursor

# Get the directory of this script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Activate the virtual environment
source "$SCRIPT_DIR/.venv/bin/activate"

# Run the calculator server
python "$SCRIPT_DIR/calculator_server.py" 