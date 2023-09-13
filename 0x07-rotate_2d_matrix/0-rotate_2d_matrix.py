#!/usr/bin/env python3
""" Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    num_rows = len(matrix)

    # Transpose the matrix (swap rows with columns)
    for i in range(num_rows):
        for j in range(i, num_rows):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row to complete the 90-degree clockwise rotation
    for row in range(num_rows):
        matrix[row].reverse()

    # print rotated matrix
    for row in matrix:
        return row
