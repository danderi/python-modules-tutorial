# utils.py
def add_numbers(a, b):
    """Sum two numbers"""
    return a + b

def multiply_numbers(a, b):
    """Multiply two numbers"""
    return a * b


# app.py
from utils import add_numbers, multiply_numbers
from validator import validate_numbers

def main():
    # Performing calculations
    a, b = 4, 3
    if validate_numbers(a, b):
        print(add_numbers(a, b))  # Should print 7
        print(multiply_numbers(a, b))  # Should print 12
    else:
        print("Invalid numbers")

# Call the main function to run the program
if __name__ == "__main__":
    main()


# validator.py
def validate_numbers(a, b):
    """Check if the numbers are valid"""
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        return False
    return True

