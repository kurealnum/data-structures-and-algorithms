def mergeSort(arr):
    arr_len = len(arr)

    if arr_len > 1:
        left_arr = arr[:arr_len//2]
        right_arr = arr[arr_len//2:]

        #recursion
        mergeSort(left_arr)
        mergeSort(right_arr)

        print(mergeSort(left_arr),mergeSort(right_arr))

        #merge
        i = j = k = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1

            else:
                arr[k] = right_arr[j]
                j += 1

            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

        return arr


arr = [2,5,3,6,1,4,8,7]

arr = mergeSort(arr)
print(arr)