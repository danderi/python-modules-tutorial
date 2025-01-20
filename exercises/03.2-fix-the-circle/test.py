import pytest
from io import StringIO
from unittest.mock import patch
import app  # Import the application file

# Test to verify that the functions are imported correctly
@pytest.mark.it("Check if the functions are imported correctly from utils and validator")
def test_imports():
    try:
        from utils import add_numbers, multiply_numbers  # Check if the functions are imported correctly
        from validator import validate_numbers
    except ImportError:
        pytest.fail("It seems there is an error with the imports. Make sure the functions are properly imported from the corresponding files (utils.py and validator.py).")

# Test to check if the main function is defined in app.py 
@pytest.mark.it("Ensure that the 'main' function is defined in app.py")
def test_main_function():
    assert hasattr(app, 'main'), "The 'main' function is missing in app.py. Make sure it's correctly defined."


# Test to verify calculations and validation work as expected
@pytest.mark.it("Verify that the calculations and validation are working correctly")
def test_calculations_and_validation():
    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        # Simulate execution with valid numbers
        app.main()  # Call the main function

        output = mock_stdout.getvalue()
        assert "7" in output, "The addition is not working correctly. Make sure the sum is being performed correctly."
        assert "12" in output, "The multiplication is not working correctly. Make sure the multiplication is being performed correctly."
        assert "Invalid numbers" not in output, "You should not see the 'Invalid numbers' message if the numbers are valid."
