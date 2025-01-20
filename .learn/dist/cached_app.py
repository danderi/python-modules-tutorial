# This is our entry point file! This file is where our program starts running
from helper import greet # First, we import what we need from our helper module


def main():
   # add your code here
   name = input("Please enter your name: ")


   
   if len(name) < 3:
      print("Your name is quite short! Are you sure that's correct?")

   if name == "Teacher":
      print("Welcome Teacher, are you ready to guide your students?")

   print("Nice to meet you! Let's start learning Python!")
