# This is our calculator module
from utils import validate_numbers

def add_numbers(a, b):
    """Add two numbers if they are valid"""
    if validate_numbers(a, b):
        return a + b
    return "Invalid input"

def multiply_numbers(a, b):
    """Multiply two numbers if they are valid"""
    if validate_numbers(a, b):
        return a * b
    return "Invalid input"

# Test the calculator
if __name__ == "__main__":
    print(add_numbers(4, 3))
    print(multiply_numbers(4, 3))