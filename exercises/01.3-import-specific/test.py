import unittest
from unittest.mock import patch
from io import StringIO
import sys

class TestRandomChoice(unittest.TestCase):
    @patch('random.choice', return_value='apple')
    def test_random_choice(self, mock_choice):
        # Capture the output
        captured_output = StringIO()
        sys.stdout = captured_output
        
        # Import the module to test
        import app
        
        # Reset redirect.
        sys.stdout = sys.__stdout__
        
        # Check the output
        self.assertEqual(captured_output.getvalue().strip(), 'apple')

if __name__ == '__main__':
    unittest.main()