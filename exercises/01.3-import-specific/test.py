import pytest
from unittest.mock import patch
from io import StringIO
import importlib

@pytest.mark.it("Should import the random module")
def test_random_module_import():
    try:
        import app  # Import the file that contains your main code
        assert "random" in dir(app), "The random module is not imported"
    except ImportError:
        pytest.fail("The random module is not imported in app.py")



@pytest.mark.it("Should use print to output the result")
def test_print_output():
    with patch('random.choice', return_value='apple'):
        with patch("sys.stdout", new_callable=StringIO) as stdout:
            import app  # Importa el archivo que contiene tu código principal
            importlib.reload(app)  # Reimporta el módulo para asegurar que se ejecute el código
            output = stdout.getvalue().strip()
    assert output == 'apple', f"The output is not as expected. Got: {output}"

