# NumT

NumT is a powerful Python utility library for formatting numbers, currencies, dates, units, and more. It provides a simple and consistent interface for handling various numerical formatting needs.

## Features

- Currency formatting with support for multiple formats (Western, Indian, Continental, Swiss)
- SI unit conversions and formatting for length, mass, and time
- Number to word conversion with support for short and long formats
- Human-readable number formatting with customizable precision

## Installation

NumT is available on PyPI and can be installed using pip:

```bash
pip install numt
```

Or using Poetry:

```bash
poetry add numt
```

## Usage Examples

### Currency Formatting

```python
from numt import format_currency

# Western format (default)
print(format_currency(1234567.89))  # $1,234,567.89

# Indian format
print(format_currency(1234567.89, format_type="indian"))  # ₹12,34,567.89

# Continental format
print(format_currency(1234567.89, format_type="continental"))  # €1.234.567,89

# Swiss format
print(format_currency(1234567.89, format_type="swiss"))  # CHF 1'234'567.89
```

### SI Unit Conversions

```python
from numt import convert_si, Length, Mass, Time

# Length conversions
length = Length(1500, "m")
print(length.format())  # 1.50 km

# Mass conversions
mass = Mass(0.5, "kg")
print(mass.format())  # 500.00 g

# Time conversions
time = Time(3660, "s")
print(time.format())  # 1.02 h

# Direct conversion
result = convert_si(1000, "m", "km", "length")
print(result)  # 1.0
```

### Number Formatting

```python
from numt import to_words

# Short format
print(to_words(1234567))  # 1.23 M
print(to_words(1234567, format_type="long"))  # 1.23 million

# With precision
print(to_words(1234567, precision=1))  # 1.2 M

# Strip zero cents
print(to_words(1000.00, strip_zero_cents=True))  # 1 K
```

## Development

### Setup Development Environment

1. Clone the repository:
```bash
git clone https://github.com/yourusername/numt.git
cd numt
```

2. Install dependencies using Poetry:
```bash
poetry install
```

3. Install pre-commit hooks:
```bash
poetry run pre-commit install
```

### Running Tests

```bash
poetry run pytest
```

### Building the Package

```bash
poetry build
```

## Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details on how to submit pull requests, report issues, and suggest improvements.

## Code of Conduct

Please read our [Code of Conduct](CODE_OF_CONDUCT.md) to keep our community approachable and respectable.

## License

This project is licensed under the terms of the [LICENSE](LICENSE) file.

## Changelog

See the [CHANGELOG.md](CHANGELOG.md) file for a list of changes between versions.
