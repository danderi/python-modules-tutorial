# 🛠️ Fix the Circular Import

Now that we've seen the circular import error, let's fix it! We'll learn how to reorganize our code to avoid the circular dependency.

## 📝 Instructions

1. **Understand the circular import problem.** Review the files `app.py` and `validator.py`. Both files try to import functions from each other, causing a circular import error. We need to reorganize the code to avoid this.

2. **Identify what each file does.** 
- `app.py`: Contains calculation functions like `add_numbers` and `multiply_numbers`. These functions receive numbers, validate them, and then perform operations.

- `validator.py`: Contains the `validate_numbers` function, which checks if the provided numbers are valid before performing an operation. However, this file tries to use calculation functions (like `multiply_numbers`), creating a cycle.

3. **Separate the logic into different files.** To avoid the circular import, we will reorganize the code.

- Refactor the `add_numbers` and `multiply_numbers` functions to be pure mathematical functions without any validation. Then move them to `utils.py`.

`utils.py` should look like this:

```python
# utils.py

def add_numbers(a, b):
    """Add two numbers"""
    return a + b

def multiply_numbers(a, b):
    """Multiply two numbers"""
    return a * b
```

- Now, in `validator.py`, we will keep only the validation logic. We do not need the calculation functions here. Copy this code into `validator.py`:

```python
# validator.py
def validate_numbers(a, b):
    """Check if the numbers are valid"""
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        return False
    return True
```

4. **Refactor the `app.py` file.** Import the calculation functions (`add_numbers`, `multiply_numbers`) from `utils.py` and the validation function `validate_numbers` from `validator.py`.

5. Define a function called `main` to make the code more organized. This function should be the entry point of the program and should do the following:

- Validate the numbers using `validate_numbers`.
- If they are valid, perform addition and multiplication with the `add_numbers` and `multiply_numbers` functions.
- If they are not valid, display a message indicating that the numbers are invalid. Example:

```python
a, b = 4, 3
if validate_numbers(a, b):
    print(add_numbers(a, b))  
    print(multiply_numbers(a, b)) 
else:
    print("Invalid numbers")
```


## ✅ Expected Output

When running `app.py`:

```python
7  # Result of 4 + 3
12 # Result of 4 * 3
```

If you followed these instructions successfully, it means you separated the responsibilities of calculation and validation functions into different modules. This not only eliminates the circular import problem but also makes your code more organized and easier to maintain.
