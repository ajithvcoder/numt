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


def percent_of(value, percent):
    """
    Calculate the percentage of a given value.

    Args:
        value (float): The base number.
        percent (float): The percentage to calculate (e.g., 25 for 25%).

    Returns:
        float: Result of the percentage calculation.
    """
    return (percent / 100) * value


def percentile(data, percentile_rank):
    """
    Calculate the value at a given percentile.

    Args:
        data (list): Sorted list of numbers.
        percentile_rank (float): Percentile (0-100).

    Returns:
        float: Value at the specified percentile.
    """
    if not data:
        raise ValueError("Data list is empty")
    k = (len(data) - 1) * (percentile_rank / 100)
    f = int(k)
    c = f + 1
    if c >= len(data):
        return data[f]
    d0 = data[f] * (c - k)
    d1 = data[c] * (k - f)
    return d0 + d1


def percentage_change(old, new):
    """
    Calculate the percentage change between two values.

    Args:
        old (float): Original value.
        new (float): New value.

    Returns:
        float: Percentage change (positive or negative).
    """
    if old == 0:
        raise ValueError("Old value cannot be zero")
    return ((new - old) / old) * 100


def percent_rank(data, value):
    """
    Compute the percentage rank of a value within a dataset.

    Args:
        data (list): List of values.
        value (float): Value to find rank for.

    Returns:
        float: Percent rank (0-100).
    """
    if not data:
        raise ValueError("Data list is empty")
    count = sum(1 for x in data if x < value)
    return (count / len(data)) * 100


def value_percentiles_with_duplicates(data):
    """
    Calculate the percentile rank for each value in a dataset,
    handling duplicates appropriately (equal values get equal percentile ranks).
    Uses the "midrank" strategy for ties (like NumPy/SciPy’s rankdata(method='average')).

    Args:
        data (list): List of numeric values.

    Returns:
        list of dict: Each dict contains 'value' and 'percentile'.
    """
    if not data:
        raise ValueError("Data list is empty")

    sorted_data = sorted(data)
    n = len(sorted_data)

    # Precompute percentile rank for each unique value
    value_to_percentile = {}
    for i, val in enumerate(sorted_data):
        if val not in value_to_percentile:
            # All values strictly less than val
            count_less = sum(1 for x in sorted_data if x < val)
            count_equal = sorted_data.count(val)
            avg_rank = count_less + (count_equal - 1) / 2
            percentile = (avg_rank / (n - 1)) * 100 if n > 1 else 100.0
            value_to_percentile[val] = percentile

    # Build result for original data
    return [{"value": val, "percentile": value_to_percentile[val]} for val in data]


def apply_discount(price, discount_percent):
    """
    Calculate the price after a discount.

    Args:
        price (float): Original price.
        discount_percent (float): Discount percentage (e.g., 20 for 20%).

    Returns:
        float: Discounted price.
    """
    return price - (price * discount_percent / 100)


def calculate_discount_amount(list_price, net_price):
    """
    Calculate the discount value given the original and net prices.

    Args:
        list_price (float): Original price before discount.
        net_price (float): Final price after discount.

    Returns:
        float: Discount amount.
    """
    if list_price < 0 or net_price < 0:
        raise ValueError("Prices cannot be negative")
    if net_price > list_price:
        raise ValueError("Net price cannot be greater than list price")

    return list_price - net_price
