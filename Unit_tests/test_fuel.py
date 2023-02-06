from fuel import gauge, convert
import pytest

def test_convert():
    assert convert("50/100") == 50
    assert convert("1/100") == 1
    assert convert ("100/100") == 100
    assert convert ("13/20") == 65

def test_convert_ZeroDivErrro ():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_convert_ValueError ():
    with pytest.raises(ValueError):
        convert("a/b")


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"

