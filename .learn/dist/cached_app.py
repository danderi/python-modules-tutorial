# import the constants module
from constants import PI, GRAVITY, AUTHOR
# Define the function to calculate the area of a circle
def calculate_circle_area(radius):
    return PI * radius ** 2

# Define the function to calculate the fall time
def calculate_fall_time(height):
    return (2 * height / GRAVITY) ** 0.5


area = calculate_circle_area(5)
print(f"Area of a circle with radius 5: {area}")
time = calculate_fall_time(100)
print(f'Time to fall from 100 meters: {time} seconds')
print(f"These calculations were made by: {AUTHOR}")