# This is our validator module
from app import multiply_numbers  # This import creates a circle!

def validate_numbers(a, b):
    """Check if inputs are valid numbers"""
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        return False

    # Use multiply_numbers as part of validation (this creates the circular import!)
    result = multiply_numbers(a, 1)
    return result != "Invalid input"

# Test the validator
if __name__ == "__main__":
    print(validate_numbers(5, 3))
    print(validate_numbers("not a number", 3))
