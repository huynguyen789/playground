# Building MCP Servers with Python

This repository provides a step-by-step guide on how to create Model Context Protocol (MCP) servers using Python. MCP allows you to build custom tools that AI assistants like Claude and GPT can use directly.

The calculator example included here demonstrates the core concepts in a simple, easy-to-understand way.

## What is MCP?

The Model Context Protocol (MCP) is an open protocol that lets developers create custom tools for AI assistants. With MCP, you can:

- Extend AI capabilities with your own Python functions
- Connect AI assistants to your data, APIs, and services
- Create domain-specific tools for specialized tasks

MCP connects AI assistants with your custom tools:

```
+----------------+    requests    +----------------+
|                | -------------> |                |
| AI Assistant   |                | MCP Server     |
| (Claude/GPT)   |                | (Your Python   |
|                | <------------- | Functions)     |
+----------------+    results     +----------------+
```

## How to Build an MCP Server

### Step 1: Set Up Your Environment

```bash
# Create a virtual environment
uv venv
source .venv/bin/activate

# Install the MCP SDK
uv pip install mcp[cli]
```

### Step 2: Create Your Server File

Create a Python file (e.g., `my_server.py`) with this basic structure:

```python
from mcp.server.fastmcp import FastMCP

# Create an MCP server with a name
mcp = FastMCP("My Server Name")

# Define your tools using the @mcp.tool() decorator
@mcp.tool()
def my_tool(param1: str, param2: int) -> str:
    """
    Clear description of what this tool does.
    
    Input: Description of parameters
    Process: What the tool does
    Output: What the tool returns
    """
    # Your tool implementation
    return f"Processed {param1} {param2} times"

# Optional: Define resources using @mcp.resource()
@mcp.resource("resource://path")
def get_resource() -> str:
    """Provide static data as a resource."""
    return "Resource data here"

# Run the server
if __name__ == "__main__":
    mcp.run()
```

### Step 3: Test Your Server

```bash
# Run in development mode
mcp dev my_server.py

# Or create a test client
# See example_client.py in this repository
```

## Example: Calculator Server

This repository includes a simple calculator server that demonstrates the core MCP concepts:

```python
@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b

@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divide one number by another."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

The calculator example shows:
- How to define tools with proper type hints
- How to document tools for AI understanding
- How to handle errors properly
- How to organize related tools in a server

## Integrating with Cursor

### Step 1: Create a wrapper script

```bash
#!/bin/bash
# File: run_server.sh

# Get the directory of this script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Activate the virtual environment
source "$SCRIPT_DIR/.venv/bin/activate"

# Run the server
python "$SCRIPT_DIR/my_server.py"
```

### Step 2: Add to Cursor via UI
1. Open Cursor
2. Go to Settings > Features > MCP
3. Click "+ Add new MCP server"
4. Fill in the form:
   - **Type**: stdio
   - **Name**: Your server name
   - **Command**: Full path to your wrapper script
5. Click "Add"

### Step 3: Project-specific configuration
Create a `.cursor/mcp.json` file:

```json
{
  "mcpServers": {
    "myserver": {
      "command": "./run_server.sh"
    }
  }
}
```

## Best Practices for MCP Servers

1. **Clear Documentation**: Write detailed docstrings for all tools
2. **Type Hints**: Always use proper type hints for parameters and return values
3. **Error Handling**: Handle errors gracefully with clear error messages
4. **Single Responsibility**: Each tool should do one thing well
5. **Testing**: Write tests for all your tools
6. **Security**: Be careful with tools that modify data or access sensitive information

## Advanced MCP Features

- **Async Tools**: Use `async def` for non-blocking operations
- **Resources**: Provide static data through resources
- **Context**: Access request context in your tools
- **Lifespan**: Manage server startup and shutdown

## Next Steps

After mastering the basics with this calculator example, try building more complex MCP servers:
- Database query tools
- API integration tools
- File manipulation tools
- Data analysis tools

## Repository Contents

- `calculator_server.py`: Example MCP server implementation
- `example_client.py`: Client to test the server
- `test_calculator.py`: Unit tests
- `run_mcp_server.sh`: Wrapper script for Cursor integration
- `run_dev.sh`: Script to run the server in development mode

## Resources

- [MCP Documentation](https://modelcontextprotocol.io/)
- [MCP Specification](https://spec.modelcontextprotocol.io/)
- [Cursor](https://cursor.sh/)

## License

MIT 