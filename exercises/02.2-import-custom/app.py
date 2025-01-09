# 🔄 Let's use our custom greetings module!
# First, import the functions from our greetings module
# Add your import statement below:
from greetings import say_hello, say_goodbye

# Create a list of names
names = ["Alice", "Bob", "Charlie"]  # Add some names to this list!

# Loop through the names and greet each person
# Add your code below:
for name in names:
    print(say_hello(name))
    print(say_goodbye(name))
    print("-" * 20)  # Add a separator line between people


# Don't modify this section 👇
if __name__ == "__main__":
    # Your code will run when you execute this file
    pass