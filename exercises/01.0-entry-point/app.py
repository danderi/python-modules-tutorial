# This is our entry point file! This file is where our program starts running
from helper import greet # First, we import what we need from our helper module


def main():
   # add your code here
   name = input("What is your name:")
   if name.lower() == "teacher":
      print("Welcome teacher, are you ready to guide your students?")
   elif len(name) < 3:
      print("Your name is quite short! Are you sure that's correct?`")
   else:
      print("Nice to meet you! Let's start learning Python!")
   greet(name)

# This special if statement makes sure our code only runs when we execute this file directly
if __name__ == "__main__":
    main()