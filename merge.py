

def mergesort(arr):
    if len(arr)==1:
        return arr

    mid = round(len(arr)/2)

    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    merged = []
    i = 0
    j = 0
    k = 0
    while (i < len(left)) and (j < len(right)):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
        k += 1
    # if left is not finished or right is not finished
    while i < len(left):
        merged.append(left[i])
        i += 1
        k += 1
    while j < len(right):
        merged.append(right[j])
        j += 1
        k += 1
    return merged

arr=[1,3,4,2,10]
print("Original array is :",arr)
sorted_array=mergesort(arr)
print("Sorted array is :",sorted_array)