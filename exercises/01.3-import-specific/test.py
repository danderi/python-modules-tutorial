import pytest
from unittest.mock import patch
from io import StringIO
import importlib
from random import choice

@pytest.mark.it("Should import choice from the random module")
def test_random_choice_import():
    try:
        import app  # Import the file that contains your main code
        assert "choice" in dir(app), "The function choice from the random module is not imported"
    except ImportError:
        pytest.fail("The function choice from the random module is not imported in app.py")



@pytest.mark.it("Should use print to output the result")
def test_print_output():
    possible_fruits = ["apple", "banana", "orange", "grape"]
    with patch('random.choice', return_value='apple'):
        with patch("sys.stdout", new_callable=StringIO) as stdout:
            import app  
            importlib.reload(app) 
            output = stdout.getvalue().strip()
    assert output in possible_fruits, f"The output is not as expected. Got: {output}"

