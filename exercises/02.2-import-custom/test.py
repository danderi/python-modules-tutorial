import unittest
from io import StringIO
import sys
from greetings import say_hello, say_goodbye

class TestGreetingsLoop(unittest.TestCase):
    def test_greetings_loop(self):
        # Capture the output
        captured_output = StringIO()
        sys.stdout = captured_output
        
        # Create a list of names
        names = ["Alice", "Bob", "Charlie"]
        
        # Loop through the names and greet each person
        for name in names:
            print(say_hello(name))
            print(say_goodbye(name))
        
        # Reset redirect.
        sys.stdout = sys.__stdout__
        
        # Check the output
        expected_output = (
            "Hello, Alice!\nGoodbye, Alice!\n"
            "Hello, Bob!\nGoodbye, Bob!\n"
            "Hello, Charlie!\nGoodbye, Charlie!\n"
        )
        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()