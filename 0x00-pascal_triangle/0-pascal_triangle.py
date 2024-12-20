#!/usr/bin/python3
"""
Pascals triangle Function
"""


def pascal_triangle(n):
    """
    Returns a pascal triangle represented by a list of lists.
    """
    if type(n) is not int or n <= 0:
        return []

    result = []

    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            elif i > 0 and j > 0:
                row.append(result[i - 1][j - 1] + result[i - 1][j])
        result.append(row)

    return result
