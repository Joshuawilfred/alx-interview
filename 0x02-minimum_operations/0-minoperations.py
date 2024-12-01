#!/usr/bin/python3
"""Module that defines the minimum operations function"""


def minOperations(n):
    """Calculates the fewest number of operations
    needed to result in exactly n H characters in the file."""
    if not isinstance(n, int):
        return 0
    operations = 0
    clipboard = 0
    done = 1
    while done < n:
        if clipboard == 0:
            clipboard = done
            done += clipboard
            operations += 2
        elif n - done > 0 and (n - done) % done == 0:
            clipboard = done
            done += clipboard
            operations += 2
        elif clipboard > 0:
            done += clipboard
            operations += 1

    return operations
