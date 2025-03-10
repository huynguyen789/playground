#!/usr/bin/env python3
"""
Calculator MCP Server

This file implements a simple calculator server using the Model Context Protocol (MCP).
It provides basic arithmetic operations as tools that can be called by LLMs.
"""

import math
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Calculator")

@mcp.tool()
def add(a: float, b: float) -> float:
    """
    Add two numbers.
    
    Input: Two numbers a and b
    Process: Adds a and b together
    Output: The sum of a and b
    """
    return a + b

@mcp.tool()
def subtract(a: float, b: float) -> float:
    """
    Subtract one number from another.
    
    Input: Two numbers a and b
    Process: Subtracts b from a
    Output: The difference between a and b
    """
    return a - b

@mcp.tool()
def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers.
    
    Input: Two numbers a and b
    Process: Multiplies a and b
    Output: The product of a and b
    """
    return a * b

@mcp.tool()
def divide(a: float, b: float) -> float:
    """
    Divide one number by another.
    
    Input: Two numbers a and b
    Process: Divides a by b
    Output: The quotient of a divided by b
    
    Raises an error if b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

@mcp.tool()
def power(base: float, exponent: float) -> float:
    """
    Raise a number to a power.
    
    Input: A base number and an exponent
    Process: Raises the base to the power of the exponent
    Output: The result of base^exponent
    """
    return math.pow(base, exponent)

@mcp.tool()
def square_root(number: float) -> float:
    """
    Calculate the square root of a number.
    
    Input: A non-negative number
    Process: Calculates the square root
    Output: The square root of the input number
    
    Raises an error if the number is negative.
    """
    if number < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return math.sqrt(number)

@mcp.tool()
def modulo(a: float, b: float) -> float:
    """
    Calculate the remainder when dividing one number by another.
    
    Input: Two numbers a and b
    Process: Calculates a modulo b
    Output: The remainder when a is divided by b
    
    Raises an error if b is zero.
    """
    if b == 0:
        raise ValueError("Cannot perform modulo with zero divisor")
    return a % b

@mcp.resource("calculator://help")
def get_calculator_help() -> str:
    """
    Provide help information about the calculator.
    
    Input: None
    Process: Returns a string with help information
    Output: Help text describing available operations
    """
    return """
    Calculator MCP Server
    
    This server provides the following operations:
    - add(a, b): Add two numbers
    - subtract(a, b): Subtract b from a
    - multiply(a, b): Multiply two numbers
    - divide(a, b): Divide a by b
    - power(base, exponent): Raise base to the power of exponent
    - square_root(number): Calculate the square root of a number
    - modulo(a, b): Calculate a modulo b
    
    All operations accept and return floating-point numbers.
    """

def main():
    """
    Main entry point for the calculator server.
    
    Input: None
    Process: Runs the MCP server
    Output: None
    """
    mcp.run()

if __name__ == "__main__":
    main() 