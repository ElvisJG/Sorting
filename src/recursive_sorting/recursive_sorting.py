# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    merged_arr = []
    # Indexes at the left and right hand start at 0
    lhs = 0
    rhs = 0
    # While the length of the left hand side and right hand side do not exceed the lhs and rhs index, run
    while lhs < len(arrA) > 0 and rhs < len(arrB):
        # if the first item in lhs > first item in rhs
        if arrA[lhs] > arrB[rhs]:
            # append first item from rhs into the merged array and increase the rhs index
            merged_arr.append(arrB[rhs])
            rhs += 1
        # else if the left hand side is smaller, add that to the array and increase the lhs index
        else:
            merged_arr.append(arrA[lhs])
            lhs += 1

        # If the lhs index has run through every card on the left, meaning none are left and the entirety of the lhs
        # is inside of merged array, append rhs to merged array
        if lhs >= len(arrA):
            merged_arr += arrB[rhs:]
        # if the rhs index is greater than or equal to the index, merge the rest of the LHS
        elif rhs >= len(arrB):
            merged_arr += arrA[lhs:]

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Only run the merge if the array is greater than or equal to 2. An array with a length of 1 or less is already
    # sorted
    if len(arr) <= 1:
        return arr

    # If the length of the array is only 2, we sample the array and create a new array to send into the merge function
    if len(arr) == 2:
        sample = [[num] for num in arr]
        return merge(sample[0], sample[1])

    # We need to use floor division instead of division for arrays (/ can create floats)
    center = len(arr) // 2
    # The center is found and we take the left hand side from the center and the right hand side from the center
    # We return the final merge of the sorted halves
    return merge(merge_sort(arr[:center]), merge_sort(arr[center:]))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    return arr
