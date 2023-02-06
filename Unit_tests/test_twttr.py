from twttr import shorten

def test_twttr():
    assert shorten("mateo") == "mt"
    assert shorten("MATEO") == "MT"
    assert shorten("download") == "dwnld"
    assert shorten("course") == "crs"
    assert shorten("Eric123") == "rc123"
    assert shorten("DEV,./") == "DV,./"