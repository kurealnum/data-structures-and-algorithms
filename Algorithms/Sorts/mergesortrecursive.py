'''
def merge(C,D):
    #return array
    B = []

    i = 0
    j = 0
    for k in range(len(C+D)):
        print(B)
        if C[i] < D[j]: 
            B[k].append(C[i])
            i += 1

        else: #else D[j] < C[i]
            B[k].append(C[j])
            j += 1

    return B


def sort(arr):
    print(arr)
    if len(arr) == 1:
        return arr
    
    elif len(arr) == 2:
        if arr[1] < arr[0]:
            temp = arr[1]
            arr[1] = arr[0]
            arr[0] = temp

    return sort(arr)


arr = [2,5,3,6,1,4,8,7]
C = sort(arr[len(arr)//2:])
D = sort(arr[:len(arr)//2])
merge(C,D)
'''

def mergeSort(arr):
    arr_len = len(arr)

    if arr_len > 1:
        left_arr = arr[:arr_len//2]
        right_arr = arr[arr_len//2:]

        #recursion
        mergeSort(left_arr)
        mergeSort(right_arr)

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

print(mergeSort(arr))