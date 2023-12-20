#!/usr/bin/python3
def add(a, b):
    """
    This function adds two numbers.

    >>> add(2, 3)
    5
    >>> add(0, 0)
    0
    >>> add(-1, 1)
    0
    """
    # eg 5 is what is expected. Doctest adds the two
    #and compares the result to 5
    return a + b

if __name__ == "__main__":
    import doctest
    doctest.testmod()
