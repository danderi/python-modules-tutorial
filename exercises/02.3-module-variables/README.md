# 🌟 Module Variables and Constants

Modules can also have variables and constants. Let's learn how to create, use, and share them between files.

## 📝 Instructions

1. Create a file named `constants.py` at the same level as the `app.py` file and define these constants:

```python
PI = 3.14159
GRAVITY = 9.81
AUTHOR = "Your name"
```

2. In your main file, `app.py`, import the constants **PI, GRAVITY, AUTHOR** from `constants.py`.

3. Create the following two functions in the `app.py` file:

- `calculate_circle_area(radius)`. This function should use the **PI** constant to calculate and return the area of a circle with the given radius. The formula is: `PI * radius ** 2`. Example:

```python
def calculate_circle_area(radius):
    return PI * radius ** 2  # Use the constant PI
```

- `calculate_fall_time(height)`. This function should use the **GRAVITY** constant to calculate and return the time it takes for an object to fall from a given height using the physics formula: `(2 * height / GRAVITY) ** 0.5`. Similar to what we did in the previous step.

4. Call the `calculate_circle_area` function with a radius of **5**. Save the result and print a message like:

```python
area = calculate_circle_area(radius)

print(f"Area of a circle with radius 5: {area}.")
```

5. Similarly, call the `calculate_fall_time` function with a height of **100** meters. Save the result and print a message like:

```python
"Time to fall from 100 meters: 4.52 seconds."
```

6. Finally, print a message with the **AUTHOR** constant to indicate who created these functions. Example:

```python
print(f"These calculations were made by: {AUTHOR}")
```

## ✅ Expected Output

Your program should print something like:

```python
Area of a circle with radius 5: 78.54
Time to fall from 100 meters: 4.52 seconds
These calculations were made by: Your Name
```

## 💡 Tips

Constants are generally written in uppercase letters. Example:
```python
PI = 3.14159
GRAVITY = 9.81
```
