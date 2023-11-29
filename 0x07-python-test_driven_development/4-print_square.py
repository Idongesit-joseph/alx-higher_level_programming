#!/usr/bin/python3
def print_square(size):
    """print square with the # character.

    Args:
        size (int):  ppp
    Raise:
        TypeError:jjj
        valueError: ddd
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise valueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
