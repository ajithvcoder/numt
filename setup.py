from setuptools import setup, find_packages

setup(
    name='numt',
    version='0.1.0',
    description='Utility library for formatting values like numbers, dates, units, etc.',
    author='ajithvcoder',
    packages=find_packages(),
    install_requires=[
        'phonenumbers',
        'babel',         # for currency/date locales
    ],
)
