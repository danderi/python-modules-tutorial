import unittest
from io import StringIO
import sys
from greetings import say_hello, say_goodbye

class TestGreetings(unittest.TestCase):
    def test_greetings(self):
        # Capture the output
        captured_output = StringIO()
        sys.stdout = captured_output
        
        # Call the functions
        print(say_hello("Alice"))
        print(say_goodbye("Alice"))
        
        # Reset redirect.
        sys.stdout = sys.__stdout__
        
        # Check the output
        expected_output = "Hello, Alice!\nGoodbye, Alice!\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()