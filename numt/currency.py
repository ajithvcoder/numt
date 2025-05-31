from numt.common.constants import currency_symbols


def format_currency(amount, currency="USD", precision=2, format_type="western"):
    """
    Format number as currency.

    Args:
        amount (float): Amount to format
        currency (str): Currency code (USD, EUR, etc.)
        precision (int): Number of decimal places
        format_type (str): Format type (western, indian, continental, swiss)

    Returns:
        str: Formatted currency
    """
    symbol = currency_symbols.get(currency, currency + " ")

    # Handle negative numbers
    is_negative = amount < 0
    print(amount)
    print("amount")
    print(is_negative)
    amount = abs(amount)

    if format_type == "western":
        formatted_amount = f"{amount:,.{precision}f}"
    elif format_type == "indian":

        def indian_format(n, precision):
            s = f"{n:.{precision}f}"
            if "." in s:
                integer_part, decimal_part = s.split(".")
            else:
                integer_part, decimal_part = s, ""
            rev = integer_part[::-1]
            groups = [rev[:3]]
            rev = rev[3:]
            while rev:
                groups.append(rev[:2])
                rev = rev[2:]
            formatted_int = ",".join(groups)[::-1]
            return formatted_int + ("." + decimal_part if decimal_part else "")

        formatted_amount = indian_format(amount, precision)
    elif format_type == "continental":
        formatted_amount = (
            f"{amount:,.{precision}f}".replace(",", "X")
            .replace(".", ",")
            .replace("X", ".")
        )
    elif format_type == "swiss":
        formatted_amount = (
            f"{amount:,.{precision}f}".replace(",", "X")
            .replace(".", ",")
            .replace("X", "'")
        )
    else:
        formatted_amount = f"{amount:,.{precision}f}"

    # Add negative sign if needed
    if is_negative:
        return f"-{symbol}{formatted_amount}"

    return f"{symbol}{formatted_amount}"
