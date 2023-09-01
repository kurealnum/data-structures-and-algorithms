from helpers import Helpers

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
visited = set()


def dfs(r: int, c: int):
    if Helpers.is_valid(matrix, r, c) or (r, c) in visited:
        return

    visited.add((r, c))
    for dr, dc in directions:
        dfs(r + dr, c + dc)


dfs(0, 0)
