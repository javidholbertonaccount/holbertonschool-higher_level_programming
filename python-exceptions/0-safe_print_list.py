#!/usr/bin/python3
"""Module that contains safe_print_list function."""


def safe_print_list(my_list=[], x=0):
    """Prints x elements of a list."""
    count = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            count += 1
    except IndexError:
        pass
    print()
    return count
