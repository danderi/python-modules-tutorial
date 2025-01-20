import pytest
from unittest.mock import patch
from io import StringIO

@pytest.mark.it("Should import the random module")
def test_random_module_import():
    try:
        import app  # Import the file that contains your main code
        assert "random" in dir(app), "The random module is not imported"
    except ImportError:
        pytest.fail("The random module is not imported in app.py")

@pytest.mark.it("Should generate a random number between 1 and 10 and print it")
def test_random_number_generation():
    with patch("random.randint", return_value=5):
        with patch("sys.stdout", new_callable=StringIO) as stdout:
            import importlib
            import app  # Import the file that contains your main code
            importlib.reload(app)  # Reimport the module to ensure the code runs
            output = stdout.getvalue().strip()
    assert output == "5", "The output is not the expected number"