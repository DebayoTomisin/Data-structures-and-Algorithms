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
            del (arr[i])
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

"""Write a program that calculates the sum of numbers recursively"""


def sum_recursive(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + sum_recursive(arr[1:])


print('')
print(array2)
print(sum_recursive(array2))

"""Write a function that converts a number to any base"""


def to_base(n, base):
    convert_string = "0123456789ABCDEF"
    if n < base:
        return convert_string[n]
    else:
        return to_base(n // base, base) + convert_string[n % base]


print(to_base(10, 8))
print('')
"""Write a function to get the sum of a non negative integer"""

number = 12344

string_num = str(number)
total = 0
for i in range(len(string_num)):
    num = int(string_num[i])
    total += num

print(total)


def sum_string(figure):
    if figure == 0:
        return 0
    else:
        return figure % 10 + sum_string(int(figure / 10))


print(sum_string(number))
print('')
print('')
"""Write a python function to calculate the sum of positive integer of n"""


def positive_integers(n):
    sum_ = 0
    for i in range(n + 1):
        if i % 2 == 0:
            sum_ += i
    return sum_


def recursive_positive(n):
    if n < 1:
        return 0
    else:
        return n + recursive_positive(n - 2)


print(recursive_positive(10))
print(positive_integers(10))

sum_ = 0
for i in range(10 + 1):
    if i % 2 == 0:
        sum_ += i
print(sum_)


def binary_search(arr, item):
    high = len(arr) - 1
    low = 0
    while low <= high:
        middle = high + low
        value = arr[middle]
        if value == item:
            return middle
        else:
            if value < item:
                low = middle + 1
            else:
                high = middle - 1
    return None


def binary_DC(arr, x):
    low = 0
    high = len(arr) - 1

    if low <= high:
        mid = low + high
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
            return binary_DC(arr[mid:], x)
        else:
            high = mid - 1
            return binary_DC(arr[:mid], x)
    else:
        return None


def maxim_num(arr):
    index = 0
    big = arr[0]
    for i in range(0, len(arr)):
        if big < arr[i]:
            big = arr[i]
            index = i
    return index


# print('This is array 1', array2)
# print('maximum value in this array is set at ', maxim_num(array2))
# num = [3]
# print('')
# print('the base case of the maximum number function is,', maxim_num(num))
# sort_list = [1, 3, 4, 9, 10, 19]
# print('The result of the binary search algorithm is ', binary_search(sort_list, 9))
# print('')
# print('')
# print('the recursive binary search is ', binary_DC(sort_list, 9))


'''Singly Linked List Implementation'''


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def printLL(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


print('')
print('')
LL = LinkedList()
LL.insert(3)
LL.insert(4)
LL.insert(5)
LL.printLL()