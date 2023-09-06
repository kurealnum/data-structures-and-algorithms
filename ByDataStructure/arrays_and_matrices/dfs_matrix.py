# DFS is weird on a matrix, because a basic linear scan is basically DFS...
# but if you're looking for say, a chain of numbers, then DFS is certainly different than a linear scan.
from helpers import Helpers

h = Helpers()

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
visited = set()


def dfs(r: int, c: int):
    if h.is_valid(matrix, r, c) or (r, c) in visited:
        return

    visited.add((r, c))
    for dr, dc in directions:
        dfs(r + dr, c + dc)


dfs(0, 0)
