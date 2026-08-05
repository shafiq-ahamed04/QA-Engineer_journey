
import pytest

def test_equal():
    assert 5 == 5

def test_not_equal():
    assert 5 != 3

def test_true():
    assert True == True

def test_false():
    assert False == False

def test_in():
    assert 4 in [1,2,3,4]

def test_str():
    assert "python" in "hello python "


def divide():
    return 20 / 0

def test_exception():
    with pytest.raises(ZeroDivisionError):
        divide()

def test_fail():
    assert 5 == 10