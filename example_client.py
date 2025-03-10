#!/usr/bin/env python3
"""
Example MCP client for the Calculator Server.

This script demonstrates how to use the MCP client to interact with the calculator server.
It connects to the server, lists available tools, and performs some calculations.
"""

import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    """
    Main function that demonstrates client usage.
    
    Input: None
    Process: Connects to the calculator server and performs operations
    Output: Calculation results
    """
    # Create server parameters for stdio connection
    server_params = StdioServerParameters(
        command="python",
        args=["calculator_server.py"],
        env=None
    )

    print("Connecting to calculator server...")
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()
            print("Connected to calculator server!")

            # List available tools
            tools_response = await session.list_tools()
            print("\nAvailable calculator tools:")
            
            # Extract the actual tools list from the response
            if hasattr(tools_response, 'tools') and tools_response.tools:
                for tool in tools_response.tools:
                    print(f"- {tool.name}: {tool.description.strip()}")
            else:
                print("No tools found or unexpected response format")

            # Read the help resource
            print("\nReading help resource...")
            resource_response = await session.read_resource("calculator://help")
            
            # Extract the text content from the response
            if isinstance(resource_response, tuple) and len(resource_response) > 0:
                contents = resource_response[0]
                if isinstance(contents, tuple) and len(contents) > 1 and contents[0] == 'contents':
                    text_contents = contents[1][0].text
                    print("Help content:")
                    print(text_contents)
                else:
                    print("Unexpected resource response format")
            else:
                print("Unexpected resource response format")

            # Perform some calculations
            print("\nPerforming calculations:")
            
            # Helper function to extract result from tool response
            def extract_result(response):
                if hasattr(response, 'content') and response.content:
                    for content in response.content:
                        if hasattr(content, 'text'):
                            return content.text
                return str(response)
            
            # Addition
            result = await session.call_tool("add", {"a": 5, "b": 3})
            print(f"5 + 3 = {extract_result(result)}")
            
            # Subtraction
            result = await session.call_tool("subtract", {"a": 10, "b": 4})
            print(f"10 - 4 = {extract_result(result)}")
            
            # Multiplication
            result = await session.call_tool("multiply", {"a": 6, "b": 7})
            print(f"6 * 7 = {extract_result(result)}")
            
            # Division
            result = await session.call_tool("divide", {"a": 20, "b": 4})
            print(f"20 / 4 = {extract_result(result)}")
            
            # Power
            result = await session.call_tool("power", {"base": 2, "exponent": 8})
            print(f"2^8 = {extract_result(result)}")
            
            # Square root
            result = await session.call_tool("square_root", {"number": 144})
            print(f"√144 = {extract_result(result)}")
            
            # Modulo
            result = await session.call_tool("modulo", {"a": 17, "b": 5})
            print(f"17 % 5 = {extract_result(result)}")
            
            print("\nAll calculations completed successfully!")

if __name__ == "__main__":
    asyncio.run(main()) 