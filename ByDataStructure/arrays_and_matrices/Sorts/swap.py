#just a basic swap function
def swap(arr: list, i: int, j: int) -> None:
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

