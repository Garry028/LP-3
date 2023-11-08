# Give an algorithm that sort given set of elements in O(nlogn). Repeat the experiment for different values of n. Verify the best, average and worst-case complexity, read element list from a file or generated using the random number generator

# best case O(nlogn)
# average case o(nlogn)
# average case o(n^2)

def sort(nums, low, high):
    if low >= high:
        return

    s = low
    e = high
    m = round(s+(e-s)/2)
    pivot = nums[m]  # mid will be pivot

    while s <= e:
        # If already sorted it will not swap
        # means ele at start is less than pivot element then move start ahead
        while nums[s] < pivot:
            s += 1
        # means ele at end is greater than pivot element then move end behind
        while nums[e] > pivot:
            e -= 1
        # if start is still less than end then swap them
        if s <= e:
            temp = nums[s]
            nums[s] = nums[e]
            nums[e] = temp
            s += 1
            e -= 1
            # now pivot is at correct index please sort two halfs now
    sort(nums, low, e)
    sort(nums, s, high)


arr = [-3, 4, 3, 2,100,192,9321,12321,33]
sort(arr, 0, len(arr)-1)

print(arr)
