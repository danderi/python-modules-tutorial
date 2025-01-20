import pytest
from unittest.mock import patch
from io import StringIO

@pytest.mark.it("Should import the say_hello and say_goodbye functions")
def test_import_say_hello():
    try:
        from greetings import say_hello, say_goodbye
        
        assert callable(say_hello), "say_hello is not callable"
        assert callable(say_goodbye), "say_goodbye is not callable"
    except ImportError:
        pytest.fail("The module greetings.py could not be imported.")


@pytest.mark.it("Should print the results of say_hello and say_goodbye in app.py")
def test_app_prints_greetings():
    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        import app  # Import the file that contains your main code
        output = mock_stdout.getvalue().strip().split("\n")  # Capture each line of the standard output

    # Define the expected values in the correct order
    expected = [
        "Hello, Alice!",
        "Goodbye, Alice!"
    ]

    assert output == expected, f"Expected output to be '{expected}', but got '{output}'"
