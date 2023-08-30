#!/usr/bin/python3
"""N queens module
"""
import sys


solutions = []
"""List of solutions
"""
n = 0
"""size of the board
"""
pos = None
"""List of possible positions on the board
"""


def get_input():
    """Get input from command line
    """
    global n
    n = 0
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)
    if n < 4:
        print('N must be at least 4')
        exit(1)
    return n


def is_attacking(pos1, pos2) -> bool:
    """Checks if two positions are attacking each other
    Args:
        pos1 (tuple): position 1
        pos2 (tuple): position 2
    """
    return pos1[0] == pos2[0] or pos1[1] == pos2[1] or \
        abs(pos1[0] - pos2[0]) == abs(pos1[1] - pos2[1])


def group_exists(group):
    """Checks if a group of positions already exists
    """
    global solutions
    for solution in solutions:
        i = 0
        for solution_pos in solution:
            for group_pos in group:
                if solution_pos[0] == group_pos[0] and \
                        solution_pos[1] == group_pos[1]:
                    i += 1
        if i == n:
            return True
    return False


def build_solution(row, group):
    """Builds a solution for the n queens problem

    Args:
        row (int): current row in the board 
        group (list): list of positions
    """
    global solutions
    global n
    if row == n:
        if not group_exists(group):
            solutions.append(group.copy())
    else:
        for col in range(n):
            pos = (row, col)
            if not any(
                is_attacking(pos, group_pos) \
                    for group_pos in group
                ):
                group.append(pos)
                build_solution(row + 1, group)
                group.remove(pos)

def get_solutions():
    """Returns the solutions for the n queens problem
    """
    global n
    global pos
    pos = list(map(lambda x: [x // n, x % n], range(n ** 2)))
    build_solution(0, [])
    

n = get_input()
get_solutions()
for solution in solutions:
    print(solution)
