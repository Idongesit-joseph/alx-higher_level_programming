#!/usr/bin/python3
def safe_print_integer(value):
    """print an integer with "{:d}".format().

    Args:
        value (int): fff

    Return:
        fffff
    """

    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
