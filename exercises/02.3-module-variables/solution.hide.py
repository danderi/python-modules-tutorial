# Import the constants from the constants.py file
from constants import PI, GRAVITY, AUTHOR

# Define the function to calculate the area of a circle
def calculate_circle_area(radius):
    return PI * radius * radius  # Use the constant PI

# Define the function to calculate the fall time
def calculate_fall_time(height):
    return (2 * height / GRAVITY) ** 0.5  # Use the constant GRAVITY


# Calculate the area of a circle with radius 5
radius = 5
area = calculate_circle_area(radius)
print(f"Area of a circle with radius {radius}: {area:.2f}")

# Calculate the fall time from a height of 100 meters
height = 100
time = calculate_fall_time(height)
print(f"Time to fall from {height} meters: {time:.2f} seconds")

# Print the author
print(f"These calculations were made by: {AUTHOR}")

