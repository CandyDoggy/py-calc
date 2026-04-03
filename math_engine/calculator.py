"""
Math engine for the calculator.
Supports basic arithmetic, scientific functions, and symbolic math.
"""

import math
from typing import Union
from sympy import sympify, Symbol, symbols, simplify, N
from sympy.core.sympify import SympifyError
import numpy as np


class CalculatorError(Exception):
    """Custom exception for calculator errors."""
    pass


class Calculator:
    """Math engine supporting basic, scientific, and symbolic calculations."""
    
    def __init__(self):
        self.history = []
        self.max_history = 100
        self.x = Symbol('x')
        self.y = Symbol('y')
    
    def evaluate(self, expression: str) -> str:
        """
        Evaluate a mathematical expression.
        
        Args:
            expression: The mathematical expression to evaluate
            
        Returns:
            The result as a string
        """
        try:
            # Clean the expression
            expr = expression.strip()
            if not expr:
                return ""
            
            # Replace common math functions with sympy equivalents
            expr = self._preprocess_expression(expr)
            
            # Parse and evaluate
            result = sympify(expr, locals={'x': self.x, 'y': self.y})
            
            # Try to evaluate numerically if it's a number
            try:
                numeric_result = N(result)
                if numeric_result.is_number and not numeric_result.has(Symbol):
                    # Format the result
                    if numeric_result.is_integer:
                        result_str = str(int(numeric_result))
                    else:
                        result_str = str(float(numeric_result))
                else:
                    result_str = str(result)
            except (TypeError, ValueError):
                result_str = str(result)
            
            # Add to history
            self._add_to_history(expression, result_str)
            
            return result_str
            
        except SympifyError as e:
            raise CalculatorError(f"Invalid expression: {expression}")
        except Exception as e:
            raise CalculatorError(f"Error: {str(e)}")
    
    def _preprocess_expression(self, expr: str) -> str:
        """Preprocess expression to handle common math notation."""
        # Replace common functions
        replacements = {
            'sin': 'sin',
            'cos': 'cos',
            'tan': 'tan',
            'asin': 'asin',
            'acos': 'acos',
            'atan': 'atan',
            'log': 'log',
            'ln': 'ln',
            'sqrt': 'sqrt',
            'exp': 'exp',
            'pi': 'pi',
            'e': 'E',
            '^': '**',
        }
        
        for old, new in replacements.items():
            expr = expr.replace(old, new)
        
        return expr
    
    def _add_to_history(self, expression: str, result: str):
        """Add calculation to history."""
        self.history.append((expression, result))
        if len(self.history) > self.max_history:
            self.history.pop(0)
    
    def get_last_calculation(self) -> tuple:
        """Get the most recent calculation."""
        if self.history:
            return self.history[-1]
        return None
    
    def get_history(self) -> list:
        """Get calculation history."""
        return self.history.copy()
    
    def clear_history(self):
        """Clear calculation history."""
        self.history = []
    
    def solve_equation(self, equation: str, variable: str = 'x') -> str:
        """
        Solve an equation symbolically.
        
        Args:
            equation: The equation to solve (e.g., "x**2 - 4 = 0")
            variable: The variable to solve for
            
        Returns:
            The solution(s) as a string
        """
        try:
            from sympy import solve, Eq
            
            # Split by equals sign
            if '=' in equation:
                left, right = equation.split('=', 1)
                eq = Eq(sympify(left.strip()), sympify(right.strip()))
            else:
                eq = sympify(equation)
            
            var = symbols(variable)
            solutions = solve(eq, var)
            
            if not solutions:
                return "No solution found"
            
            result = ', '.join(str(s) for s in solutions)
            return f"{variable} = {result}"
            
        except Exception as e:
            raise CalculatorError(f"Error solving equation: {str(e)}")
    
    def derivative(self, expression: str, variable: str = 'x') -> str:
        """
        Calculate the derivative of an expression.
        
        Args:
            expression: The expression to differentiate
            variable: The variable to differentiate with respect to
            
        Returns:
            The derivative as a string
        """
        try:
            from sympy import diff
            
            var = symbols(variable)
            expr = sympify(expression, locals={variable: var})
            result = diff(expr, var)
            return str(result)
            
        except Exception as e:
            raise CalculatorError(f"Error calculating derivative: {str(e)}")
    
    def integral(self, expression: str, variable: str = 'x') -> str:
        """
        Calculate the indefinite integral of an expression.
        
        Args:
            expression: The expression to integrate
            variable: The variable to integrate with respect to
            
        Returns:
            The integral as a string
        """
        try:
            from sympy import integrate
            
            var = symbols(variable)
            expr = sympify(expression, locals={variable: var})
            result = integrate(expr, var)
            return f"{result} + C"
            
        except Exception as e:
            raise CalculatorError(f"Error calculating integral: {str(e)}")
    
    def simplify_expression(self, expression: str) -> str:
        """
        Simplify a mathematical expression.
        
        Args:
            expression: The expression to simplify
            
        Returns:
            The simplified expression
        """
        try:
            expr = sympify(expression)
            result = simplify(expr)
            return str(result)
        except Exception as e:
            raise CalculatorError(f"Error simplifying: {str(e)}")
