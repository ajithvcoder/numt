from numt.currency import format_currency


def test_western_currency_format():
    assert format_currency(1234567.89) == "$1,234,567.89"
    assert format_currency(1234567.89, currency="EUR") == "€1,234,567.89"
    assert format_currency(1234567.89, currency="GBP") == "£1,234,567.89"


def test_indian_currency_format():
    assert (
        format_currency(1234567.89, currency="INR", format_type="indian")
        == "₹12,34,567.89"
    )


def test_continental_currency_format():
    assert (
        format_currency(1234567.89, currency="EUR", format_type="continental")
        == "€1.234.567,89"
    )


def test_swiss_currency_format():
    assert (
        format_currency(1234567.89, currency="CHF", format_type="swiss")
        == "F1'234'567,89"
    )


def test_precision():
    assert format_currency(1234567.89, precision=0) == "$1,234,568"
    assert format_currency(1234567.89, precision=3) == "$1,234,567.890"


def test_negative_numbers():
    assert format_currency(-1234567.89) == "-$1,234,567.89"
    assert format_currency(-1234567.89, "INR", format_type="indian") == "-₹12,34,567.89"


def test_zero():
    assert format_currency(0) == "$0.00"
    assert format_currency(0, precision=0) == "$0"
