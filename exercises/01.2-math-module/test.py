import unittest
from unittest.mock import patch
from io import StringIO
import sys

class TestMathModule(unittest.TestCase):
    @patch('math.sqrt', return_value=4.0)
    @patch('math.pi', new_callable=lambda: 3.141592653589793)
    def test_math_operations(self, mock_sqrt, mock_pi):
        # Capture the output
        captured_output = StringIO()
        sys.stdout = captured_output
        
        # Import the module to test
        import app
        
        # Reset redirect.
        sys.stdout = sys.__stdout__
        
        # Check the output
        expected_output = "The square root of 16 is: 4.0\nTwo times pi is: 6.283185307179586\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()