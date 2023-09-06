from collections import deque
from helpers import Helpers as help

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def isValid(visited: set, row: int, col: int, height: int, width: int) -> bool:
    # If cell lies out of bounds
    if row < 0 or col < 0 or row >= width or col >= height:
        return False

    # If cell is already visited
    if visited[row][col]:
        return False

    # Otherwise
    return True


def bfs(grid: list[list], row: int, col: int) -> None:
    q = deque()
    dRow = [-1, 0, 1, 0]
    dCol = [0, 1, 0, -1]

    # starting cell
    visited = [[False for i in range(len(grid[0]))] for i in range(len(grid))]
    visited[row][col] = True
    q.append((row, col))

    while len(q) > 0:
        # the removal/setup process
        cell = q.popleft()
        x = cell[0]
        y = cell[1]
        print(grid[x][y], end=" ")

        # checking the possibly adjacent cells
        for i in range(len(grid)):
            adjx = x + dRow[i]
            adjy = y + dCol[i]
            # add to queue and visited if it wasn't visited already
            if isValid(visited, adjx, adjy, len(grid), len(grid[i])):
                q.append((adjx, adjy))
                visited[adjx][adjy] = True


bfs(matrix, 0, 0)
