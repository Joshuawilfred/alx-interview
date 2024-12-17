#!/usr/bin/python3
"""
Implementation of a method that determines if a given
data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """Checks if data is a valid UTF-8 encoding.
    """
    check = 0

    for byte in data:
        ones = 1 << 7

        if check == 0:

            while ones & byte:
                check += 1
                ones = ones >> 1

            if check == 0:
                continue

            if check == 1 or check >= 5:
                return False

        else:
            if not (byte & 0b10000000 and not (byte & 0b01000000)):
                return False

            check -= 1

    if check == 0:
        return True

    return False
