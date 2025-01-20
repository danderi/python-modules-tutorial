import pytest
from unittest.mock import patch
from io import StringIO
import importlib

@pytest.mark.it("Should import the math module")
def test_math_module_import():
    try:
        import app  # Import the file that contains your main code
        assert "math" in dir(app), "The math module is not imported"
    except ImportError:
        pytest.fail("The math module is not imported in solution.py")

@pytest.mark.it("Should use math.sqrt() and math.pi and print the correct results")
def test_math_operations():
    with patch("sys.stdout", new_callable=StringIO) as stdout:
        import app  # Import the file that contains your main code
        importlib.reload(app)  # Reimport the module to ensure the code runs
        output = stdout.getvalue().strip()
    expected_output = "The square root of 16 is: 4.0\nTwo times pi is: 6.283185307179586"
    assert output == expected_output, f"The output is not as expected. Got: {output}"
