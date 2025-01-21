from io import StringIO
import pytest
from unittest.mock import patch

@pytest.mark.it("Should check that 'say_hello' and 'say_goodbye' functions are imported in app")
def test_functions_import():
    import app  # Import the app module
    # Check that 'say_hello' and 'say_goodbye' functions are imported in 'app'
    assert hasattr(app, 'say_hello'), "say_hello is not imported in app"
    assert hasattr(app, 'say_goodbye'), "say_goodbye is not imported in app"

@pytest.mark.it("Should declare the 'names' array in app.py")
def test_names_array_declaration():
    import app  # Import the app module
    import importlib
    importlib.reload(app)  # Reload the module to ensure it reflects recent changes
    
    assert hasattr(app, 'names'), "'names' array is not declared in app.py"
    
    # Check that 'names' is a list
    assert isinstance(app.names, list), "'names' is not a list"
    
    # Check that the 'names' array contains the expected elements
    expected_names = ["Alice", "Bob", "Charlie"]
    assert app.names == expected_names, f"'names' array does not match the expected: {expected_names}. Actual: {app.names}"


@pytest.mark.it("Should print the results of say_hello and say_goodbye in app.py") 
def test_app_prints_greetings(app):
    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        app()
        # Capture what was printed
        output = mock_stdout.getvalue().strip().split("\n")  # Capture each line of the standard output

    # Define the expected values in the correct order
    expected = [
        "Hello, Alice!",
        "Goodbye, Alice!",
        "Hello, Bob!",
        "Goodbye, Bob!",
        "Hello, Charlie!",
        "Goodbye, Charlie!"
    ]

    # Verify that the output is as expected
    assert output == expected, f"Expected output to be '{expected}', but got '{output}'"
