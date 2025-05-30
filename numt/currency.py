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
