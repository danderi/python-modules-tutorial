# This is our shared utilities module

def is_valid_number(value):
    """Check if a value is a valid number"""
    return isinstance(value, (int, float))

def validate_numbers(a, b):
    """Check if both inputs are valid numbers"""
    return is_valid_number(a) and is_valid_number(b)
