# utils.py
def is_valid_number(value):
    return isinstance(value, (int, float))

def validate_numbers(a, b):
    return is_valid_number(a) and is_valid_number(b)

# calculator.py
from utils import validate_numbers

def add_numbers(a, b):
    if validate_numbers(a, b):
        return a + b
    return "Invalid input"

def multiply_numbers(a, b):
    if validate_numbers(a, b):
        return a * b
    return "Invalid input"

# validator.py
from utils import validate_numbers

def validate_calculation(func, a, b):
    if validate_numbers(a, b):
        result = func(a, b)
        return isinstance(result, (int, float))
    return False
