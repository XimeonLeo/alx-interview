#!/usr/bin/python3
""" This module defines the Pascal's Triangle '"""


def pascal_triangle(n):
    """
        Generate Pascal's Triangle with n rows

        Parameter:
            n: the size of the triangle

        Return:
            a list of lists of integers representing the
            Pascal’s triangle of n

            an empty list if n <= 0
    """
    List = []
    for i in range(n):
        """ Creating the outer list """
        lists = []
        for j in range(i + 1):
            """ Creating the inner lists """
            if j == 0 or j == i:
                lists.append(1)
            else:
                lists.append(List[i - 1][j - 1] + List[i - 1][j])
        List.append(lists)
    return List
