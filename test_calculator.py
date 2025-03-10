#!/usr/bin/env python3
"""
Test script for the Calculator MCP Server.

This script tests the basic functionality of the calculator server
by importing the server module and directly calling its functions.
"""

import unittest
from calculator_server import add, subtract, multiply, divide, power, square_root, modulo

class TestCalculator(unittest.TestCase):
    """
    Test case for the calculator functions.
    
    Input: Calculator functions
    Process: Tests each function with various inputs
    Output: Test results (pass/fail)
    """
    
    def test_add(self):
        """Test the add function."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(2.5, 3.5), 6.0)
    
    def test_subtract(self):
        """Test the subtract function."""
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(1, 1), 0)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(5.5, 2.5), 3.0)
    
    def test_multiply(self):
        """Test the multiply function."""
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(2.5, 2), 5.0)
    
    def test_divide(self):
        """Test the divide function."""
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(5, 2), 2.5)
        self.assertEqual(divide(0, 5), 0)
        with self.assertRaises(ValueError):
            divide(5, 0)
    
    def test_power(self):
        """Test the power function."""
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(2, 0), 1)
        self.assertEqual(power(0, 5), 0)
        self.assertEqual(power(4, 0.5), 2.0)
    
    def test_square_root(self):
        """Test the square_root function."""
        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(0), 0)
        self.assertEqual(square_root(2), 1.4142135623730951)
        with self.assertRaises(ValueError):
            square_root(-1)
    
    def test_modulo(self):
        """Test the modulo function."""
        self.assertEqual(modulo(7, 3), 1)
        self.assertEqual(modulo(8, 4), 0)
        self.assertEqual(modulo(5.5, 2), 1.5)
        with self.assertRaises(ValueError):
            modulo(5, 0)

if __name__ == "__main__":
    unittest.main() 