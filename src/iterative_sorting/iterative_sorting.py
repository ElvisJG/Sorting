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
    # Initiates swap boolean
    swap = True
    # Begins code and will run until swap is false
    while swap:
        # Swap is set to false, this will terminate the code if the swap is not set to true in the following loop
        swap = False
        # iterates through the given array starting at position 0 and stopping at position 10 (9)
        for i in range(0, len(arr) - 1):
            # Syntactic sugar, instantiating 2 vars
            lhs = i
            rhs = i + 1
            # from the array using the index we see if the left hand side is greater than the right hand side
            if arr[lhs] > arr[rhs]:
                # if so we create a new variable to hold the left hand side and initiate a swap
                # left hand goes to hold
                hold = arr[lhs]
                # right hand goes to left
                arr[lhs] = arr[rhs]
                # left hand goes to right
                arr[rhs] = hold
                # since this swap happened, we set swap to true causing this loop to re-fire
                swap = True

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    return arr
