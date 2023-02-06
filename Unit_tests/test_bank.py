from bank import value

def test_hello():
    assert value("hello") == 0

def test_hop():
    assert value("hop") == 20

def test_HOP():
    assert value("HOP") == 20

def test_hop_hop():
    assert value("hop hop") == 20

def test_yo():
    assert value("yo") == 100

def test_Yo_Man():
    assert value("Yo Man") == 100

def test_other():
    assert value("Yo Man!&*(^&") == 100