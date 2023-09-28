#!/usr/bin/python3
"""island perimeter module.
"""


def island_perimeter(grid):
    """returns the perimeter of the island described in grid.
    """
    if type(grid) != list or len(grid) <= 0:
        return 0
    if not all(map(lambda x: type(x) == list and len(x) > 0, grid)):
        return 0
    if not all(map(lambda x: all(map(lambda y: y == 0 or y == 1, x)), grid)):
        return 0
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
    return perimeter
