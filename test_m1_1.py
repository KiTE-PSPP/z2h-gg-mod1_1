import pytest
import m1_1  

def test_print_welcome(capsys):
    expected_output = "Welcome to Guessing game"

    m1_1.print_welcome()
    captured = capsys.readouterr()

    assert expected_output in captured.out
