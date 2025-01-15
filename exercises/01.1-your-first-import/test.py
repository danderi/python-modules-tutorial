import unittest
from unittest.mock import patch
from io import StringIO
import sys
import app
import random

class TestApp(unittest.TestCase):
    @patch('random.randint', return_value=5)
    @patch('sys.stdout', new_callable=StringIO)
    def test_random_number(self, mock_stdout, mock_randint):
        # Capture the output
        captured_output = mock_stdout
        
        # Call the function
        app.random_number = random.randint(1, 10)
        print(app.random_number)
        
        # Check the output
        self.assertEqual(captured_output.getvalue().strip(), '5')

    @patch('random.randint', return_value=7)
    @patch('sys.stdout', new_callable=StringIO)
    def test_random_number_seven(self, mock_stdout, mock_randint):
        # Capture the output
        captured_output = mock_stdout
        
        # Call the function
        app.random_number = random.randint(1, 10)
        print(app.random_number)
        
        # Check the output
        self.assertEqual(captured_output.getvalue().strip(), '7')

    @patch('random.randint', return_value=10)
    @patch('sys.stdout', new_callable=StringIO)
    def test_random_number_ten(self, mock_stdout, mock_randint):
        # Capture the output
        captured_output = mock_stdout
        
        # Call the function
        app.random_number = random.randint(1, 10)
        print(app.random_number)
        
        # Check the output
        self.assertEqual(captured_output.getvalue().strip(), '10')

if __name__ == "__main__":
    unittest.main()