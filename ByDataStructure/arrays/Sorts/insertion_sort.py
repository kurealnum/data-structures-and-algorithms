def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def insertion_sort(arr):
    for i in range(1, len(arr)):
        
        key = arr[i]
        j = i-1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key 


arr = [3,5,2,1,4,7,6]
insertion_sort(arr)
print(arr)
        
