#!/usr/bin/python3
"""method determines if given data set represents a valid UTF-8 encoding"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """returns True if data is valid UTF-8 encoding else return False"""
    for i in range(len(data)):
        if data[i] > 255:
            return False
    return True
