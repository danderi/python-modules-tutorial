# 🎬 This is our entry point file!
# This file is where our program starts running

# First, we import what we need from our helper module
from helper import greet

def main():
    """This is our main function - where our program starts"""
    # Call the greeting function from our helper module
    name = "Learner"
    greet(name)

    # Add our own message
    print("Welcome to the Python Modules tutorial! 🚀")

# This special if statement makes sure our code only runs when we execute this file directly
if __name__ == "__main__":
    main()