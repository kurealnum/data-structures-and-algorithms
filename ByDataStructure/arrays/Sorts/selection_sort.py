from swap import swap

def find_min(arr: list) -> int:
    res = arr[0]

    for i in arr:
        if res > i:
            res = i

    return res   


def selection_sort(arr: list) -> None:
    #outer iteration
    for i in range(len(arr)):
        min_idx = i

        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j

        swap(arr, i, min_idx)


if __name__ == "__main__":
    arr = [3,5,2,1,4,7,6]
    selection_sort(arr)
    print(arr)