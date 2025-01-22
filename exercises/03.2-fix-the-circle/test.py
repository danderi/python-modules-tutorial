import pytest
from io import StringIO
from unittest.mock import patch



@pytest.mark.it("Should only validate and not perform multiplication in validate_numbers")
def test_validate_numbers_does_not_multiply():
    with patch('app.multiply_numbers') as mock_multiply_numbers:
        from validator import validate_numbers
       
        a, b = 3, 4

        result = validate_numbers(a, b)
      
        mock_multiply_numbers.assert_not_called()


        assert result is True, "The validation should pass for valid numbers."


@pytest.mark.it("Should import add_numbers, multiply_numbers, and validate_numbers")
def test_constants_import():
        import app  # Import the file that contains your main code
        assert "add_numbers" in dir(app), "The function add_numbers from the utils module is not imported"
        assert "multiply_numbers" in dir(app), "The function multiply_numbers from the utils module is not imported"
        assert "validate_numbers" in dir(app), "The function validate_numbers from the validator module is not imported"



@pytest.mark.it("Ensure that the 'main' function is defined in app.py")
def test_functions_declared():
    from app import main
        
    # Verify that both functions are callable (i.e., they are defined as functions)
    assert callable(main), "The function main is not declared in app.py"
   

@pytest.mark.it("Verify that the calculations and validation are working correctly")
def test_calculations_and_validation():
    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        import app
        app.main()  # Call the main function

        output = mock_stdout.getvalue()
        assert "Invalid numbers" not in output, "You should not see the 'Invalid numbers' message if the numbers are valid."


@pytest.mark.it("the addition is not working correctly. Make sure the sum is being performed correctly.")
def test_addition_function():
    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        import app
        app.main()  # Call the main function

        output = mock_stdout.getvalue()
        assert "7" in output, "The addition is not working correctly. Make sure the sum is being performed correctly."
       

@pytest.mark.it("The multiplication is not working correctly. Make sure the multiplication is being performed correctly.")
def test_multiplication_function():
    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        import app
        app.main()  # Call the main function

        output = mock_stdout.getvalue()
        assert "12" in output, "The multiplication is not working correctly. Make sure the multiplication is being performed correctly."
