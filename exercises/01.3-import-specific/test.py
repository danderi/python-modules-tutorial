import pytest
from unittest.mock import patch
from io import StringIO
import importlib

@pytest.mark.it("Should use random.choice and print the correct result")
def test_random_choice():
    with patch('random.choice', return_value='apple'):
        with patch("sys.stdout", new_callable=StringIO) as stdout:
            import app  # Importa el archivo que contiene tu código principal
            importlib.reload(app)  # Reimporta el módulo para asegurar que se ejecute el código
            output = stdout.getvalue().strip()
    assert output == 'apple', f"The output is not as expected. Got: {output}"







# import unittest
# from unittest.mock import patch
# from io import StringIO
# import sys

# class TestRandomChoice(unittest.TestCase):
#     @patch('random.choice', return_value='apple')
#     def test_random_choice(self, mock_choice):
#         # Capture the output
#         captured_output = StringIO()
#         sys.stdout = captured_output
        
#         # Import the module to test
#         import app
        
#         # Reset redirect.
#         sys.stdout = sys.__stdout__
        
#         # Check the output
#         self.assertEqual(captured_output.getvalue().strip(), 'apple')

# if __name__ == '__main__':
#     unittest.main()