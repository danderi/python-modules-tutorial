# This is our calculator module - renamed to app.py
from validator import validate_numbers  # This import creates a circle!

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

# Try to use the functions
if __name__ == "__main__":
    print(add_numbers(5, 3))
    print(multiply_numbers(4, 2))
