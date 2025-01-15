from greetings import say_hello, say_goodbye

# Create a list of names
names = ["Alice", "Bob", "Charlie"]

# Loop through the names and greet each person
for name in names:
    print(say_hello(name))
    print(say_goodbye(name))
