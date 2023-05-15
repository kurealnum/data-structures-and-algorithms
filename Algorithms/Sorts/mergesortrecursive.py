def merge_sort(arr):
    print(arr)
    if len(arr) == 1:
        return arr
    
    elif len(arr) == 2:
        if arr[1] < arr[0]:
            temp = arr[1]
            arr[1] = arr[0]
            arr[0] = temp

    return merge_sort(arr[:len(arr)//2]) + merge_sort(arr[len(arr)//2:])

arr = [2,5,3,6,1,4,8,7]
print(merge_sort(arr))