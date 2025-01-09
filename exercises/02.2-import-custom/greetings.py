# 👋 This is our custom greetings module!
# It contains functions for different types of greetings

def say_hello(name):
    """Return a friendly hello message"""
    return f"Hello, {name}!"

def say_goodbye(name):
    """Return a friendly goodbye message"""
    return f"Goodbye, {name}!"

# This section will only run if we run this file directly
if __name__ == "__main__":
    # Test the functions
    print(say_hello("Alice"))
    print(say_goodbye("Bob"))
