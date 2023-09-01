class Helpers:
    # just swapping 2 elements
    def swap(arr: list, i: int, j: int) -> None:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    # function for checking if a movement is valid in a matrix
    def is_valid(matrix: list[list], r: int, c: int):
        return r < 0 or c < 0 or r == len(matrix) or c == len(matrix)
