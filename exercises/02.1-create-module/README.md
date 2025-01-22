# 🎨 Create Your First Module

Let's create a simple greeting module! We'll make a module that has functions to say hello in different ways.

## 📝 Instructions

1. Create a file named `greetings.py`. This file should be in the same folder as the `app.py` file for this exercise.

2. In the file named `greetings.py`, declare a function called `say_hello(name)`. This function will take a name as input and return a personalized greeting with that name. Example:

```python
def say_hello(name):
    return f"Hello, {name}!"
```

3. In the same file `greetings.py`, define another function called `say_goodbye(name)` that returns the following message:

```python
return f"Goodbye, {name}!"
```

Similar to how we did in the previous step.

4. Now, in the `app.py` file, we will import the functions we just created in `greetings.py` and use them by doing a `print()` of what each returns. Example:

```python
print(say_hello("Alice"))
```

## ✅ Expected Output

Your program should print something like:

```python
Hello, Alice!
Goodbye, Alice!
```

## 💡 Hint

The import in your `app.py` file should look something like this:

```python
# app.py

from greetings import say_hello 
```
