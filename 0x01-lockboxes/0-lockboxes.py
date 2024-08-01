#!/usr/bin/python3


""" method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """ method that determines if all the boxes can be opened.
    """
    if not boxes:
        return False
    if len(boxes) == 0:
        return False
    keys = [0]
    for key in keys:
        for box in boxes[key]:
            if box not in keys and box < len(boxes):
                keys.append(box)
    if len(keys) == len(boxes):
        return True
    return False
