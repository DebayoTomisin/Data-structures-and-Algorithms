"""Starting out with binary search algorithms"""
"""Binary search algorithms need to be used in a sorted list of elements, it returns the position of the element
being search for otherwise it return NULL"""
# Testing out the binary search function

array = [2, 6, 8, 20, 25, 32, 45]

low = 0  # minimum position of the item  being search for

high = len(array) - 1
# print(high)
item_value = 8
mid = round((low + high) / 2)
guess = array[mid]
if guess < item_value:
    low = mid + 1
    # print(low)
else:
    high = mid - 1
    # print(high)


def binary_search(arr, item):
    mini = 0
    maxim = len(arr) - 1
    while mini <= maxim:
        middle = (mini + maxim)
        value = arr[middle]
        if item == value:
            return middle
        if value > item:
            maxim = middle - 1
        else:
            mini = middle + 1
    return None


# print('the sorted array is {}'.format(array))
# print('The index of the item is:', binary_search(array, 5))

array1 = [1, 4, 5, 9, 11, 18, 22]
# print(array1)
# print(len(array1))



"""A string has unique values"""
strone = 'abba'

def uniqueStr(string):
    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            if string[i] == string[j]:
                return 'String is not unique'
    return 'string is unique'

print(uniqueStr(strone))

def optimizedStr(string):
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            return 'String is not unique'
    return 'string is unique'

print('')
print(optimizedStr(strone))