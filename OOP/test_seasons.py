from seasons import convert


def test_convert():
    assert convert(
        "2022-03-07") == "Five hundred twenty-five thousand, six hundred minutes"
    assert convert(
        "2021-03-07") == "One million, fifty-one thousand, two hundred minutes"
