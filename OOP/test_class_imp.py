from class_imp import Jar


def test_in():
    jar = Jar()
    assert jar.capacity == 12


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
#    # jar.deposit(11)
#    # assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


#
#
# def test_deposit():
#    ...
#
#
# def test_withdraw():
#    ...