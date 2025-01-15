import unittest
from unittest.mock import patch
from io import StringIO
from app import main

class TestApp(unittest.TestCase):
    @patch('builtins.input', return_value="Teacher")
    @patch('sys.stdout', new_callable=StringIO)
    def test_teacher_name(self, mock_stdout, mock_input):
        # Simula la entrada del nombre "Teacher"
        main()
        output = mock_stdout.getvalue()
        self.assertIn("Welcome, teacher ready to guide your students?", output)

    @patch('builtins.input', return_value="Jo")
    @patch('sys.stdout', new_callable=StringIO)
    def test_short_name(self, mock_stdout, mock_input):
        # Simula la entrada de un nombre corto
        main()
        output = mock_stdout.getvalue()
        self.assertIn("Your name is quite short! Are you sure that's correct?", output)

    @patch('builtins.input', return_value="Alex")
    @patch('sys.stdout', new_callable=StringIO)
    def test_regular_name(self, mock_stdout, mock_input):
        # Simula la entrada de un nombre regular
        main()
        output = mock_stdout.getvalue()
        self.assertIn("Nice to meet you! Let's start learning Python!", output)

    @patch('builtins.input', return_value="")
    @patch('sys.stdout', new_callable=StringIO)
    def test_empty_name(self, mock_stdout, mock_input):
        # Simula la entrada vacía
        main()
        output = mock_stdout.getvalue()
        self.assertIn("Hello, !", output)  # Saludo para nombre vacío
        self.assertIn("Your name is quite short! Are you sure that's correct?", output)

if __name__ == "__main__":
    unittest.main()
