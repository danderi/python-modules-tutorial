# 🔄 Using Your Custom Module

Now that we have created our greetings module, let's use it in our app.py!

## 📝 Instructions

1. Make sure you have the `greetings.py` file created. This file should contain the two functions:

- `say_hello(name)` that returns "Hello, {name}!".
- `say_goodbye(name)` that returns "Goodbye, {name}!".

2. Import the `say_hello` and `say_goodbye` functions from your `greetings.py` file. Example:

```python
#app.py
from greetings import say_hello, say_goodbye
```

3. Create a list of names:

```python
names = ["Alice", "Bob", "Charlie"]
```
4. Use a loop to iterate over the list of names to greet and say goodbye to each person.
5. Print the results of each greeting and farewell.

## ✅ Expected Output

Your program should print something like:
```python
Hello, Alice!
Goodbye, Alice!
Hello, Bob!
Goodbye, Bob!
Hello, Charlie!
Goodbye, Charlie!
```
