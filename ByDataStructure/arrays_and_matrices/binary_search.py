def binary_search(arr: list, target) -> bool:
    low = 0
    high = len(arr)-1

    while low <= high:
        
        mid = low + (high - low) // 2

        if arr[mid] == target:
            return True
        
        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1


if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9,10]

    print(binary_search(arr,5))




















































































