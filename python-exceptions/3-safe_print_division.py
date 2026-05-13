#!/usr/bin/python3
"""Module that contains safe_print_division function."""


def safe_print_division(a, b):
    """Divides 2 integers and prints the result."""
    res = None
    try:
        res = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(res))
    return res
