import pytest
from unittest.mock import patch
from io import StringIO
import app  # Importa el archivo que contiene tu código principal

@pytest.mark.it("Should warn about a very short name")
def test_short_name():
    with patch("builtins.input", return_value="Ed"):
        with patch("sys.stdout", new_callable=StringIO) as stdout:
            app.main()
            output = stdout.getvalue().strip()
    assert "Your name is quite short!" in output, "The program did not warn about short names correctly."

@pytest.mark.it("Should respond positively to a regular name")
def test_regular_name():
    with patch("builtins.input", return_value="Alice"):
        with patch("sys.stdout", new_callable=StringIO) as stdout:
            app.main()
            output = stdout.getvalue().strip()
    assert "Nice to meet you!" in output, "The program did not respond positively to a regular name."

@pytest.mark.it("Should handle empty input gracefully")
def test_empty_name():
    with patch("builtins.input", return_value=""):
        with patch("sys.stdout", new_callable=StringIO) as stdout:
            app.main()
            output = stdout.getvalue().strip()
    assert "Your name is quite short!" in output, "The program did not handle empty input correctly."

@pytest.mark.it("Should handle name input with extra spaces correctly")
def test_name_with_spaces():
    with patch("builtins.input", return_value="   John   "):
        with patch("sys.stdout", new_callable=StringIO) as stdout:
            app.main()
            output = stdout.getvalue().strip()
    assert "Nice to meet you!" in output, "The program did not handle names with extra spaces correctly."

@pytest.mark.it("Should greet the teacher with a specific message")
def test_teacher_name():
    with patch("builtins.input", return_value="Teacher"):
        with patch("sys.stdout", new_callable=StringIO) as stdout:
            app.main()
            output = stdout.getvalue().strip()
    assert "Welcome Teacher, are you ready to guide your students?" in output, "The program did not greet the teacher correctly."

