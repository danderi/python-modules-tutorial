# 🎬 Understanding Entry Points in Python

Hello! 👋 Before diving into module imports, let's understand something super important: entry points!

## 🤔 What is an entry point?

Think of your Python program as a book 📚. Just as every book needs a first page, every Python program needs a main file where everything begins. We call this the "entry point" of your program.

In our exercises, we will use `app.py` as our entry point. This is the file that:

1. 🎯 Starts your program
2. 📥 Imports other modules
3. 🎮 Controls the main flow of your program

## 💡 Example
Here is a simple example:
```python
# app.py (Your entry point)
from helper import greet  # Import from another module

def main():
    name = "Alice"
    greet(name)

if __name__ == "__main__":
    main()
```

helper.py (Another module)

```python
def greet(name):
    print(f"Hello, {name}!")
```

## Instructions

In this exercise, we will work with two pre-created files. Let's get started! 🚀

1. Look at the file named `helper.py` which contains an auxiliary function called greet(name) that simply greets the user. It is a "tool" that we will use in the main program.

2. Look at the file named **app.py:** which will be the main file serving as the entry point to the program and imports the `greet` function from helper.py and organizes the main logic in the `main()` function.

**Note:** The if __name__ == "__main__" block ensures that the program starts from here.

3. In the main file **app.py** complete the `main()` function in app.py to ask for the user's name and store it in a variable `name`.

4. Call the `greet(name)` function to greet the user.

5. Check the following in the `main()` function:

- If the name is "Teacher", display a special message. Example: `Welcome, teacher ready to guide your students?`
- If the name has fewer than 3 characters, give a warning. Example: `Your name is quite short! Are you sure that's correct? 🤔`
- If it is different from "Teacher" and has more than 3 characters, give a welcome message. Example: `Nice to meet you! Let's start learning Python! 🚀`

6. Once you have completed the logic in `main()`, run the program.

Finally, why has the organization we chose for our code been important?

- 🎯 Because it keeps the code organized
- 🔄 Clearly shows where your program starts
- 📦 Helps avoid circular imports (we will learn about them later!)

In the next exercises, we will practice importing and using modules, always starting from our entry point app.py!
