# Same as app.py - this shows the correct implementation
from helper import greet

def main():
    name = input("What is your name? ").strip()  # Ask the user for their name
    greet(name)  # Call the greet function to say hello

    # Here you can add your own logic:
    if name.lower() == "teacher":
        print("Welcome Teacher, are you ready to guide your students?")
    elif len(name) < 3:
        print("Your name is quite short! Are you sure that's correct?")
    else:
        print("Nice to meet you! Let's start learning Python!")


if __name__ == "__main__":
    main()
