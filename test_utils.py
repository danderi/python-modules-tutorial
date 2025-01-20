
def smart_stdout_asset(expected_output, stdout, messsage):
    assert expected_output.lower() in stdout.getvalue().strip().lower(), messsage
