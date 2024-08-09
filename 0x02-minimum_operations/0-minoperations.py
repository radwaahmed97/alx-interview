#!/usr/bin/python3
"""
method that calculates the fewest number of operations
needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    calculates the fewest number of operations
    needed to result in exactly n H characters in the file.
    """
    if n < 2 or type(n) is not int:
        return 0
    copy_Paste_operation_times = 1
    process_times = []
    i = n
    while i != 1:
        copy_Paste_operation_times += 1
        if i % copy_Paste_operation_times == 0:
            while (i % copy_Paste_operation_times == 0 and i != 1):
                i /= copy_Paste_operation_times
                process_times.append(copy_Paste_operation_times)
    return sum(process_times)
