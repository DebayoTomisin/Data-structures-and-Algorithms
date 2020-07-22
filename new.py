"""Problem 1 Find the maximum product of two distinct numbers in a sequence of non-negative integers. Input:
A sequence of non-negative integers. Output: The maximum value that can be obtained by multiplying two different
elements from the sequence.

Example 1: A = [3,4,3,5,6,8,9,0,1] Ans = 72 Example 2: A = [1,3,2,4] Ans = 12
"""
"""These are the various test arrays"""
value = 55
array = []
array1 = [1, -3, 0, 2, -7]
array2 = [1, 1, 4, 1, 3, 6, 7, 3, 8, 4]
array3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def duplicate(arr):  # finds the duplicate values in the list
    final_list = list()
    for num in arr:
        if num not in final_list:
            final_list.append(num)
    return final_list


def del_negative(arr):  # deletes negative values found in the list
    for i in range(len(arr) - 1):
        if arr[i] < 0:
            del(arr[i])
    return arr


def find_smallest(arr):  # this is for the selection sort algorithm, finds the smallest item in a list
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


"""Using selection sort algorithm to sort the list accordingly """


def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


def formatted(arr):
    if arr == []:
        return 'this list is empty so we cannot proceed'
    elif type(arr) != list:
        return 'Your input is not a list, please enter a list'
    else:
        del_arr = del_negative(arr)
        """check for duplicates"""
        new_list = duplicate(del_arr)
        """The approach i'll take in solving the final part is
        to sort the list and since if it's sorted the last two values will give the largest product we'll just 
        work with that"""
        sorted_list = selection_sort(new_list)
        total = sorted_list[-1] * sorted_list[-2]
        return total


print('This is a test with non lists: ', formatted(value))
print('')
print('This is the test with an empty array: ', formatted(array))
print('')
print('This is the test with a list with negative values, ', formatted(array1))
print('')
print('This is a test with duplicate values: ', formatted(array2))
print('')
print('This is a test with a good input list: ', formatted(array3))



