#!/usr/bin/python3
"""script that rotates a 2D matrix 90 degrees clockwise"""


def rotate_2d_matrix(matrix):
    """function that rotates a 2D matrix 90 degrees clockwise"""
    matrix.reverse()
    mat_len = len(matrix)
    for i in range(mat_len):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
