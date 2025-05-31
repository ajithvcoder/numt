from numt.common.constants import (
    short_numeric_suffixes,
    long_numeric_suffixes,
    short_googol_suffixes,
    long_googol_suffixes,
)


def to_words(n, precision=2, format_type="short", strip_zero_cents=False):
    """
    Convert numbers to human-readable format.

    Args:
        n (float/int): Number to convert
        precision (int): Number of decimal places
        format_type (str): 'short' for K,M,B,T or 'long' for thousand, million, etc.
        strip_zero_cents (bool): If True, removes .00 from whole numbers

    Returns:
        str: Formatted number
    """
    if n == 0:
        return "0"

    abs_n = abs(n)

    if format_type == "short":
        # Short form suffixes
        standard_suffixes = short_numeric_suffixes
        googol_suffixes = short_googol_suffixes
    else:
        # Long form suffixes
        standard_suffixes = long_numeric_suffixes
        googol_suffixes = long_googol_suffixes

    # Calculate order of magnitude
    if abs_n < 1:
        order = 0
    else:
        order = len(f"{int(abs_n)}") - 1

    if order < 100:
        # Standard -illion scaling (divide by 1000)
        idx = 0
        while abs_n >= 1000 and idx < len(standard_suffixes) - 1:
            abs_n /= 1000.0
            idx += 1
        suffix = standard_suffixes[idx]
    else:
        # Googol scaling (divide by 10^100)
        googol_power = order // 100
        power_index = min(googol_power - 1, len(googol_suffixes) - 1)
        abs_n /= 10 ** (100 * googol_power)
        if power_index < len(googol_suffixes):
            suffix = googol_suffixes[power_index]
        else:
            suffix = f"{googol_power}-googol"

    formatted_num = f"{abs_n:.{precision}f}"

    # Apply sign
    formatted_num = f"-{formatted_num}" if n < 0 else formatted_num

    # Strip .00 if requested
    if strip_zero_cents:
        if "." in formatted_num and formatted_num.endswith("0" * precision):
            formatted_num = formatted_num.split(".")[0]

    return f"{formatted_num} {suffix}".strip()
