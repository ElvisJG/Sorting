import time

def insertion_sort(numbers):

    #loop over all the numbers starting at index 1
    for i in range(1, len(numbers)):
        # save each number into a temporary variable
        current_num = numbers[i]
        
        j = i
        # loop until we reach the end of array or the number we are comparing is not smaller than its neighbor
        while j > 0 and current_num < numbers[j - 1]:
            # move the left number over to the right 1 spot
            numbers[j] = numbers[j-1]        
            j -= 1
        # save the temporary number in its correct spot
        numbers[j] = current_num

    # print(numbers)
    return numbers



def partition(numbers):
    left = []
    pivot = numbers[0]
    right = []

    for val in numbers[1:]:
        if val <= pivot:
            left.append(val)
        else:
            right.append(val)
    
    return left, pivot, right
    

def quick_sort(numbers):
    # base case
    if len(numbers) <= 1:
        return numbers

    # figure out how to split
    left, pivot, right = partition(numbers)

    # recursive case
    sorted_array = quick_sort(left) + [pivot] + quick_sort(right)
    return sorted_array





print("***********~Test with 10 numbers~**********")
start = time.time()
quick_sort([5, 6, 1, 9, 7, 2, 3, 0, 8, 10])
end = time.time()
print("Insertion Sort took:  " + str((end - start)*1000) + " milliseconds")

print("***********~Test with 100 numbers~**********")
start = time.time()
quick_sort([5, 6, 1, 9, 7, 2, 3, 0, 8, 10]*10)
end = time.time()
print("Insertion Sort took:  " + str((end - start)*1000) + " milliseconds")

print("***********~Test with 9000 numbers~**********")
start = time.time()
quick_sort([5, 6, 1, 9, 7, 2, 3, 0, 8, 10]*900)
end = time.time()
print("Insertion Sort took:  " + str((end - start)*1000) + " milliseconds")








