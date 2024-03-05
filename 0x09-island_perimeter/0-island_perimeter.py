#!/usr/bin/python3
""" This module defines a function `island_perimeter`"""


def island_perimeter(grid):
    """ Returns the perimeter of the island described in grid"""
    y_size = len(grid[0])
    x_size = len(grid)
    perimeter = 0

    for x in range(x_size):
        for y in range(y_size):
            if grid[x][y]:
                # check left-border
                if y - 1 < 0 or grid[x][y - 1] == 0:
                    perimeter += 1
                # check right-border
                if y + 1 == y_size or grid[x][y + 1] == 0:
                    perimeter += 1
                # check top-border
                if x - 1 < 0 or grid[x - 1][y] == 0:
                    perimeter += 1
                # check bottom-border
                if x + 1 == x_size or grid[x + 1][y] == 0:
                    perimeter += 1
    return perimeter
