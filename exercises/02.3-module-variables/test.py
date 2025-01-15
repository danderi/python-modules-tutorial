import unittest
from io import StringIO
import sys
from app import calculate_circle_area, calculate_fall_time
from constants import PI, GRAVITY, AUTHOR

class TestApp(unittest.TestCase):
    def test_calculations(self):
        # Capture the output
        captured_output = StringIO()
        sys.stdout = captured_output
        
        # Calculate the area of a circle with radius 5
        area = calculate_circle_area(5)
        print(f"Area of a circle with radius 5: {area:.2f}")
        
        # Calculate the fall time from 100 meters
        time = calculate_fall_time(100)
        print(f"Time to fall from 100 meters: {time:.2f} seconds")
        
        # Print the author
        print(f"These calculations were made by: {AUTHOR}")
        
        # Reset redirect.
        sys.stdout = sys.__stdout__
        
        # Check the output
        expected_output = (
            f"Area of a circle with radius 5: {PI * 5 * 5:.2f}\n"
            f"Time to fall from 100 meters: {(2 * 100 / GRAVITY) ** 0.5:.2f} seconds\n"
            f"These calculations were made by: {AUTHOR}\n"
        )
        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()