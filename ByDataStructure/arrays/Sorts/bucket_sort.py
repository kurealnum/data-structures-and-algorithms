def bucket_sort(arr):
    buckets = [[] for i in arr]
    arr_len = len(arr)

    for i in arr:
        buckets[int(arr_len*i)].append(i)

    for j in range(len(arr)):
        buckets[j] = sorted(buckets[j])

    k = 0
    for i in range(len(arr)):
        for j in range(len(buckets[i])):
            arr[k] = buckets[i][j]
            k+=1


arr = [0.32,0.22,0.66,0.25,0.31,0.44,0.37]
bucket_sort(arr)
print(arr)