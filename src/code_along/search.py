names = [
    'Anthony',
    'Artem',
    'Austin',
    'Chaz',
    'Dustin',
    'Elissa',
    'Elvis',
    'Jeffrey',
    'Justin',
    'Katherine',
    'Leslie',
    'Melvin',
    'Sandy',
    'Sheila',
    'Yi',
]

def linear_search(array, value):
    for val in array:
        if val == value:
            return True
    return False

print(linear_search(names, 'Katherine'))
print(linear_search(names, 'Sheila'))
print(linear_search(names, 'Chaz'))
print(linear_search(names, 'Doug'))

def binary_search(array, value):

    first = 0
    last = len(array) - 1
    found = False

    while first <= last and not found:
        # find the middle
        middle = (first + last) // 2
        if array[middle] == value:
            found = True
        else:
            if value < array[middle]:
                # search the lower half
                last = middle - 1
            else:
                # search the upper half of array
                first = middle + 1

    return found


print(binary_search(names, 'Katherine'))
print(binary_search(names, 'Ronny'))
print(binary_search(names, 'Justin'))
print(binary_search(names, 'Doug'))
