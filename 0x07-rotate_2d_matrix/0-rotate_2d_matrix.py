#!/usr/bin/python3
"""Rotates 2-D matrix"""


def rotate_2d_matrix(matrix):
    """Rotates in-place"""
    x = len(matrix)
    y = x - 1

    for i in range(0, int(x / 2)):
        for j in range(i, y - i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[y - j][i]
            matrix[y - j][i] = matrix[y - i][y - j]
            matrix[y - i][y - j] = matrix[j][y - i]
            matrix[j][y - i] = temp
