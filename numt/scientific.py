def format_scientific(n, precision=2):
    """
    Format number in scientific notation.

    Args:
        n (float): Number to format
        precision (int): Number of decimal places

    Returns:
        str: Formatted scientific notation
    """
    return f"{n:.{precision}e}"
