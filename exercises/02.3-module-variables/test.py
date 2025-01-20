from io import StringIO
from unittest.mock import patch
import pytest
import importlib


@pytest.mark.it("Should import the PI, GRAVITY, and AUTHOR constants")
def test_import_constants():
    from app import PI, GRAVITY, AUTHOR
        
    # Verify that the constants are defined
    assert isinstance(PI, (int, float)), "PI is not a valid number"
    assert isinstance(GRAVITY, (int, float)), "GRAVITY is not a valid number"
    assert isinstance(AUTHOR, str), "AUTHOR is not a valid string"
    

@pytest.mark.it("Should verify that the functions calculate_circle_area and calculate_fall_time are declared")
def test_functions_declared():
    from app import calculate_circle_area, calculate_fall_time
        
    # Verify that both functions are callable (i.e., they are defined as functions)
    assert callable(calculate_circle_area), "The function calculate_circle_area is not declared in app.py"
    assert callable(calculate_fall_time), "The function calculate_fall_time is not declared in app.py"
   
   

@pytest.mark.it("Should use calculate_circle_area and calculate_fall_time in app.py")
def test_app_uses_functions():
    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        # Import the app module
        import app

        # Manually call the functions to ensure they are used
        app.calculate_circle_area(5)
        app.calculate_fall_time(100)

        # Reload the module to execute the code in the main block
        importlib.reload(app)  # This makes the main code execute again

        # Capture the console output
        output = mock_stdout.getvalue()

        # Verify that the functions have been used
        assert "Area of a circle with radius 5:" in output, "The function calculate_circle_area was not used in app.py"
        assert "Time to fall from 100 meters:" in output, "The function calculate_fall_time was not used in app.py"
