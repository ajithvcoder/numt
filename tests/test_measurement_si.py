import pytest
from numt.measurement_si import Length, Mass, Time, convert_si


def test_length_conversion():
    length = Length(1500, "m")
    assert length.convert("km") == 1.5
    assert length.convert("cm") == 150000
    assert length.convert("mm") == 1500000


def test_length_format():
    length = Length(1500, "m")
    assert length.format() == "1.50 km"
    length = Length(0.5, "m")
    assert length.format() == "0.50 m"
    length = Length(0.005, "m")
    assert length.format() == "5.00 mm"


def test_mass_conversion():
    mass = Mass(1.5, "kg")
    assert mass.convert("g") == 1500
    assert mass.convert("mg") == 1500000
    assert mass.convert("t") == 0.0015


def test_mass_format():
    mass = Mass(1500, "kg")
    assert mass.format() == "1.50 t"
    mass = Mass(0.5, "kg")
    assert mass.format() == "0.50 kg"
    mass = Mass(0.005, "kg")
    assert mass.format() == "5.00 g"


def test_time_conversion():
    time = Time(3660, "s")
    assert time.convert("min") == 61
    assert time.convert("h") == 1.0166666666666666
    assert time.convert("ms") == 3660000


def test_time_format():
    time = Time(3660, "s")
    assert time.format() == "1.02 h"
    time = Time(90, "s")
    assert time.format() == "1.50 min"
    time = Time(0.005, "s")
    assert time.format() == "5.00 ms"


def test_convert_si():
    assert convert_si(1000, "m", "km", "length") == 1.0
    assert convert_si(1000, "g", "kg", "mass") == 1.0
    assert convert_si(3600, "s", "h", "time") == 1.0


def test_invalid_unit():
    with pytest.raises(ValueError):
        Length(100, "invalid_unit").convert("m")

    with pytest.raises(ValueError):
        Mass(100, "invalid_unit").convert("kg")

    with pytest.raises(ValueError):
        Time(100, "invalid_unit").convert("s")


def test_invalid_unit_type():
    with pytest.raises(ValueError):
        convert_si(100, "m", "km", "invalid_type")
