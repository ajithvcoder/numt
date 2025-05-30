def humanize_number(n, precision=2, format_type='short'):
    """
    Convert numbers to human-readable format.
    
    Args:
        n (float/int): Number to convert
        precision (int): Number of decimal places
        format_type (str): 'short' for K,M,B,T or 'long' for thousand, million, etc.
    
    Returns:
        str: Formatted number
    """
    if format_type == 'short':
        suffixes = ['', 'K', 'M', 'B', 'T']
        idx = 0
        while abs(n) >= 1000 and idx < len(suffixes)-1:
            n /= 1000.0
            idx += 1
        return f"{n:.{precision}f} {suffixes[idx]}".strip()
    else:
        suffixes = ['', 'thousand', 'million', 'billion', 'trillion']
        idx = 0
        while abs(n) >= 1000 and idx < len(suffixes)-1:
            n /= 1000.0
            idx += 1
        return f"{n:.{precision}f} {suffixes[idx]}".strip()

def format_currency(amount, currency='USD', precision=2):
    """
    Format number as currency.
    
    Args:
        amount (float): Amount to format
        currency (str): Currency code (USD, EUR, etc.)
        precision (int): Number of decimal places
    
    Returns:
        str: Formatted currency
    """
    currency_symbols = {
        'USD': '$',
        'EUR': '€',
        'GBP': '£',
        'JPY': '¥',
        'INR': '₹'
    }
    symbol = currency_symbols.get(currency, currency)
    return f"{symbol}{amount:,.{precision}f}"

def format_percentage(n, precision=1):
    """
    Format number as percentage.
    
    Args:
        n (float): Number to format (0-1)
        precision (int): Number of decimal places
    
    Returns:
        str: Formatted percentage
    """
    return f"{n * 100:.{precision}f}%"

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
