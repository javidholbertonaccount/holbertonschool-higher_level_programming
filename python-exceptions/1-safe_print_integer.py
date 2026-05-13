#!/usr/bin/python3
"""Module that contains safe_print_integer function."""


def safe_print_integer(value):
    """Prints an integer with "{:d}".format()."""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
