class SIUnit:
    """Base class for SI unit conversions"""

    UNITS = {}  # To be defined by subclasses

    def __init__(self, value, unit):
        if unit not in self.UNITS:
            raise ValueError(f"Unsupported unit: {unit}")
        self.value = value
        self.unit = unit


class Length(SIUnit):
    """Length measurements in SI units"""

    UNITS = {"m": 1.0, "km": 1000.0, "cm": 0.01, "mm": 0.001, "µm": 1e-6, "nm": 1e-9}

    def convert(self, target_unit):
        """Convert to target unit"""
        if target_unit not in self.UNITS:
            raise ValueError(f"Unsupported unit: {target_unit}")
        return self.value * (self.UNITS[self.unit] / self.UNITS[target_unit])

    def format(self, precision=2):
        """Format with appropriate unit"""
        if self.value >= 1000:
            return f"{self.convert('km'):.{precision}f} km"
        elif self.value < 0.01:
            return f"{self.convert('mm'):.{precision}f} mm"
        return f"{self.value:.{precision}f} m"


class Mass(SIUnit):
    """Mass measurements in SI units"""

    UNITS = {"kg": 1.0, "g": 0.001, "mg": 1e-6, "t": 1000.0}

    def convert(self, target_unit):
        """Convert to target unit"""
        if target_unit not in self.UNITS:
            raise ValueError(f"Unsupported unit: {target_unit}")
        return self.value * (self.UNITS[self.unit] / self.UNITS[target_unit])

    def format(self, precision=2):
        """Format with appropriate unit"""
        if self.value >= 1000:
            return f"{self.convert('t'):.{precision}f} t"
        elif self.value < 0.01:
            return f"{self.convert('g'):.{precision}f} g"
        return f"{self.value:.{precision}f} kg"


class Time(SIUnit):
    """Time measurements in SI units"""

    UNITS = {"s": 1.0, "ms": 0.001, "µs": 1e-6, "min": 60.0, "h": 3600.0}

    def convert(self, target_unit):
        """Convert to target unit"""
        if target_unit not in self.UNITS:
            raise ValueError(f"Unsupported unit: {target_unit}")
        return self.value * (self.UNITS[self.unit] / self.UNITS[target_unit])

    def format(self, precision=2):
        """Format with appropriate unit"""
        if self.value >= 3600:
            return f"{self.convert('h'):.{precision}f} h"
        elif self.value >= 60:
            return f"{self.convert('min'):.{precision}f} min"
        elif self.value < 0.01:
            return f"{self.convert('ms'):.{precision}f} ms"
        return f"{self.value:.{precision}f} s"


def convert_si(value, from_unit, to_unit, unit_type):
    """
    Convert between SI units.

    Args:
        value (float): Value to convert
        from_unit (str): Source unit
        to_unit (str): Target unit
        unit_type (str): Type of unit ('length', 'mass', 'time')

    Returns:
        float: Converted value
    """
    unit_classes = {"length": Length, "mass": Mass, "time": Time}

    if unit_type not in unit_classes:
        raise ValueError(f"Unsupported unit type: {unit_type}")

    unit_obj = unit_classes[unit_type](value, from_unit)
    return unit_obj.convert(to_unit)
