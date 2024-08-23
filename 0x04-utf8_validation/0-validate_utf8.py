#!/usr/bin/python3
"""method to check validate UTF-8 encoding"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """Returns True if data is valid UTF-8 encoding, else False"""
    number_bytes = 0

    mask_1_shift = 1 << 7
    mask_2_shift = 1 << 6

    for i in data:

        mask_byte_shift = 1 << 7

        if number_bytes == 0:

            while mask_byte_shift & i:
                number_bytes += 1
                mask_byte_shift = mask_byte_shift >> 1

            if number_bytes == 0:
                continue

            if number_bytes == 1 or number_bytes > 4:
                return False

        else:
            if not (i & mask_1_shift and not (i & mask_2_shift)):
                return False

        number_bytes -= 1

    if number_bytes == 0:
        return True

    return False
