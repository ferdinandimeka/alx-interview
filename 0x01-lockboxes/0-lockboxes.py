#!/usr/bin/python3
'''
A method that determines if all the boxes can be opened
'''

from collections import deque

def canUnlockAll(boxes):
    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    queue = deque([0]) # start with the first box
    '''
    perform BFS by popping a box from the queue, checking its keys, and adding 
    unvisited keys to the queue while marking them as visited.
    '''
    while queue:
        curr_box = queue.popleft()
        for key in boxes[curr_box]:
            if key < n and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)

