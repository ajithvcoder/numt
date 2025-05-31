from numt.numeral import to_words


def test_short_format():
    assert to_words(1234567) == "1.23 M"
    assert to_words(1234567, format_type="short") == "1.23 M"
    assert to_words(1234567890) == "1.23 B"
    assert to_words(1234567890123) == "1.23 T"


def test_long_format():
    assert to_words(1234567, format_type="long") == "1.23 million"
    assert to_words(1234567890, format_type="long") == "1.23 billion"
    assert to_words(1234567890123, format_type="long") == "1.23 trillion"


def test_precision():
    assert to_words(1234567, precision=1) == "1.2 M"
    assert to_words(1234567, precision=3) == "1.235 M"
    assert to_words(1234567, precision=0) == "1 M"


def test_strip_zero_cents():
    assert to_words(1000.00, strip_zero_cents=True) == "1 K"
    assert to_words(1000.10, strip_zero_cents=True) == "1 K"
    assert to_words(1000.00, strip_zero_cents=False) == "1.00 K"


def test_negative_numbers():
    assert to_words(-1234567) == "-1.23 M"
    assert to_words(-1234567, format_type="long") == "-1.23 million"


def test_zero():
    assert to_words(0) == "0"
    assert to_words(0, precision=2) == "0"
    assert to_words(0, format_type="long") == "0"


def test_small_numbers():
    assert to_words(0.123) == "0.12"
    assert to_words(0.123, precision=3) == "0.123"
    assert to_words(0.00123, precision=4) == "0.0012"


def test_large_numbers():
    assert to_words(1e12) == "1.00 T"
    assert to_words(1e15) == "1.00 Q"
    assert to_words(1e18) == "1.00 Qi"
