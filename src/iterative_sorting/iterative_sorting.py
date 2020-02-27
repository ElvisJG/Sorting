# TO-DO: Complete the selection_sort() function below 
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for n in range(cur_index + 1, len(arr)):
            if arr[smallest_index] > arr[n]:
                smallest_index = n

        # TO-DO: swap
        hold = arr[i]
        arr[i] = arr[smallest_index]
        arr[smallest_index] = hold

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    for i in range(0, len(arr) - 1):
        for n in range(0, len(arr) - 1):
            lhs = i;
            rhs = i + 1
            if arr[lhs] > arr[rhs]:
                hold = arr[lhs]
                arr[lhs] = arr[rhs]
                arr[rhs] = hold

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    return arr
