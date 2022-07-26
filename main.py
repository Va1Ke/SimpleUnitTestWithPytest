import pytest

def str_len(str):
    return len(str)

def test_str_len():
    test_str ="13"
    result = str_len(test_str)
    assert result == 2