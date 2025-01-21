import pytest
from unittest.mock import patch
from io import StringIO
import os


@pytest.mark.it("Should check if the greetings.py file exists")
def test_greetings_file_exists():
    file_path = "./exercises/02.1-create-module/greetings.py"
    assert os.path.isfile(file_path), "The file 'greetings.py' was not found."

@pytest.mark.it("Should import the say_hello and say_goodbye functions")
def test_greetings_import():
    try:
        import app  # Import the file that contains your main code
        assert "say_hello" in dir(app), "The function say_hello from the greetings module is not imported"
        assert "say_goodbye" in dir(app), "The function say_hello from the greetings module is not imported"
    except ImportError:
        pytest.fail("The function choice from the random module is not imported in app.py")


@pytest.mark.it("Should print the results of say_hello and say_goodbye in app.py")
def test_app_prints_greetings(app):
    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        app()
        output = mock_stdout.getvalue().strip().split("\n")  # Capture each line of the standard output

    # Define the expected values in the correct order
    expected = [
        "Hello, Alice!",
        "Goodbye, Alice!"
    ]

    assert output == expected, f"Expected output to be '{expected}', but got '{output}'"
