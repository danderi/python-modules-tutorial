import pytest
from unittest.mock import patch
from io import StringIO

@pytest.mark.it("Should import the say_hello and say_goodbye functions")
def test_import_greetings():
    try:
        from greetings import say_hello, say_goodbye
        assert callable(say_hello), "say_hello is not a function"
        assert callable(say_goodbye), "say_goodbye is not a function"
    except ImportError:
        pytest.fail("The functions say_hello and say_goodbye are not imported correctly from greetings.py")

@pytest.mark.it("The function say_hello() should return the message 'Hello, {name}!'")
@pytest.mark.parametrize("name", ["Alice", "Bob", "Charlie"])
def test_greetings(name):
    with patch("sys.stdout", new_callable=StringIO) as stdout:
        from greetings import say_hello, say_goodbye
        # Call the functions
        print(say_hello(name))
        # print(say_goodbye(name))
        
        # Get the output
        output = stdout.getvalue()
        
    # Check the output
    expected_output = f"Hello, {name}!"
    assert output == expected_output, f"The output is not as expected. Got: {output}"




@pytest.mark.it("The function say_goodbye() should return the message 'Goodbye, {name}!'")
@pytest.mark.parametrize("name", ["Alice", "Bob", "Charlie"])
def test_say_goodbye(name):
    with patch("sys.stdout", new_callable=StringIO) as stdout:
        from greetings import say_hello, say_goodbye
        # Call the functions
        print(say_goodbye(name))
        
        # Get the output
        output = stdout.getvalue()
        
    # Check the output
    expected_output = f"Goodbye, {name}!"
    assert output == expected_output, f"The output is not as expected. Got: {output}"
