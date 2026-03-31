# This is our validator module
def validate_numbers(a, b):
    """Check if the numbers are valid"""
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        return False
    return True

