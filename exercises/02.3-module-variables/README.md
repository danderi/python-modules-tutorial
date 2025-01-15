# 🌟 Module Variables and Constants

Modules can also have variables and constants. Let's learn how to create, use, and share them between files.

## 📝 Instructions

1. Create a file named `constants.py` and define these constants:

```python
PI = 3.14159
GRAVITY = 9.81
AUTHOR = "Your name"
```

2. In your main file, `app.py`, create the following two functions:
- `calculate_circle_area(radius)`. This function should use the **PI** constant to calculate and return the area of a circle with the given radius.
- `calculate_fall_time(height)`. This function should use the **GRAVITY** constant to calculate and return the time it takes for an object to fall from a given height using the physics formula: (2 * height / GRAVITY) ** 0.5
- Import the constants **PI, GRAVITY, AUTHOR** from `constants.py`.

3. Use the `calculate_circle_area` function to calculate the area of a circle with a radius of 5 and display the result.
4. Use the `calculate_fall_time` function to calculate the fall time of an object from a height of 100 meters and display the result.
5. Finally, print a message with the **AUTHOR** constant to indicate who created these functions.

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
