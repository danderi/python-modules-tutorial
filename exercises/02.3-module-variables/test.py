from io import StringIO
from unittest.mock import patch
import pytest
import importlib
import os
from unittest import mock


@pytest.mark.it("Should check if the constants.py file exists")
def test_constants_file_exists():
    file_path = "./exercises/02.3-module-variables/constants.py"
    assert os.path.isfile(file_path), "The file 'constants.py' was not found."


@pytest.mark.it("Should import the PI, GRAVITY, and AUTHOR constants")
def test_constants_import():
    try:
        import app  # Import the file that contains your main code
        assert "PI" in dir(app), "The constant PI from the constants module is not imported"
        assert "GRAVITY" in dir(app), "The constant GRAVITY from the constants module is not imported"
        assert "AUTHOR" in dir(app), "The constant AUTHOR from the constants module is not imported"
    except ImportError:
        pytest.fail("The constant PI, GRAVITY, and AUTHOR from the constants module are not imported in app.py")


@pytest.mark.it("Should verify that the constants PI, GRAVITY, and AUTHOR are declared in constants.py")
def test_constants_declared():
    try:
        import constants  # Import the constants module
        assert hasattr(constants, 'PI'), "The constant 'PI' is not defined in constants.py."
        assert hasattr(constants, 'GRAVITY'), "The constant 'GRAVITY' is not defined in constants.py."
        assert hasattr(constants, 'AUTHOR'), "The constant 'AUTHOR' is not defined in constants.py."
    except ImportError:
        pytest.fail("The constants.py file could not be imported. Check if it exists and is correctly written.")
    

@pytest.mark.it("Should verify that the functions calculate_circle_area and calculate_fall_time are declared")
def test_functions_declared():
    from app import calculate_circle_area, calculate_fall_time
        
    # Verify that both functions are callable (i.e., they are defined as functions)
    assert callable(calculate_circle_area), "The function calculate_circle_area is not declared in app.py"
    assert callable(calculate_fall_time), "The function calculate_fall_time is not declared in app.py"
   
   

@pytest.mark.it("should print the corrrect message for the area of a circle, the time to fall from 100 meters, and the author") 
def test_app_uses_functions():
    with patch("sys.stdout", new_callable=StringIO) as stdout:
        import app
        from constants import AUTHOR
        importlib.reload(app)  
        output = stdout.getvalue().strip().split("\n")

   
    assert output[0].lower() == "Area of a circle with radius 5: 78.53975".lower(), f"Unexpected output: {output[0]}"
    assert output[1].lower() == "Time to fall from 100 meters: 4.515236409857309 seconds".lower(), f"Unexpected output: {output[1]}"
    assert output[2].lower() == f"These calculations were made by: {AUTHOR}".lower(), f"Unexpected output: {output[2]}"
