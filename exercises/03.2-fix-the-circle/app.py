# This is our calculator module - renamed to app.py
from validator import validate_numbers  # This import creates a circle!
from utils import add_numbers, multiply_numbers


def main():
    a, b = 4, 3
    if validate_numbers(a, b):
        print(add_numbers(a, b))
        print(multiply_numbers(a, b))
    else:
        print("invalid numbers")



main()