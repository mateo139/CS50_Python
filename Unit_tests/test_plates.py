from plates import is_valid

def test_CS50():
    assert is_valid("CS50") == True

def test_CS05():
    assert is_valid("CS05") == False

def test_CS50P():
    assert is_valid("CS50P") == False

def test_PI():
    assert is_valid("PI3.14") == False

def test_H():
    assert is_valid("H") == False

def test_OUTATIME():
    assert is_valid("OUTATIME") == False

def test_two_letters():
    assert is_valid("C_50") == False

def test_beggining_letters():
    assert is_valid("50CS") == False
