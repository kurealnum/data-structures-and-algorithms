from helpers import Helpers

matrix = [[0, 0, 0], [0, 0, 0], [0, 1, 0]]
# directions = [[-1, 0], [-1, 0], [0, -1], [0, 1]]
directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
visited = set()


def dfs(r: int, c: int):
    if Helpers.is_valid(matrix, r, c) or (r, c) in visited:
        return

    print(matrix[r][c], r, c)
    visited.add((r, c))
    for dr, dc in directions:
        dfs(r + dr, c + dc)


dfs(0, 0)
