# This is our validator module
from utils import validate_numbers

def validate_calculation(func, a, b):
    """Validate a calculation function with given inputs"""
    if validate_numbers(a, b):
        result = func(a, b)
        return isinstance(result, (int, float))
    return False

# Test the validator
if __name__ == "__main__":
    from calculator import add_numbers, multiply_numbers
    
    print(validate_calculation(add_numbers, 5, 3))  # Should print: True
    print(validate_calculation(multiply_numbers, "not a number", 3))  # Should print: False
