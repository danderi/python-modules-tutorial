# Create your constants here
PI = 3.14159
GRAVITY = 9.81
AUTHOR = "Your Name"

def calculate_circle_area(radius):
    """Calculate the area of a circle using PI"""
    return PI * radius * radius

def calculate_fall_time(height):
    """Calculate the time it takes for an object to fall from a given height"""
    return (2 * height / GRAVITY) ** 0.5

# Test the functions
if __name__ == "__main__":
    # Calculate area of a circle with radius 5
    radius = 5
    area = calculate_circle_area(radius)
    print(f"Area of circle with radius {radius}: {area:.2f}")

    # Calculate time for an object to fall 100 meters
    height = 100
    time = calculate_fall_time(height)
    print(f"Time to fall {height} meters: {time:.2f} seconds")

    print(f"These calculations brought to you by: {AUTHOR}")