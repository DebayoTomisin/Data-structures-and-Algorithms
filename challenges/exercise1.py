import math
"""Here I'll be tackling all the exercise questions from Problem solving in DS and Algorithms  chapter 1"""
array = [1, 9, -5, 0, 12, 4]
array2 = [[1, 4, 6], [2, 3, -8, 1]]
"""1.  Find average of all the elements in a list """

def Average(arr):
    n = len(arr)
    sum = 0
    for i in range(n):
        sum += arr[i]
    average = sum / n
    return average


"""Find the sum of all the elements of a two dimensional list."""


def TwoDSum(arr):
    sum = 0
    for i in arr:
        for j in i:
           sum += j
    return sum

"""Find the largest element in a list"""

def MaxiumEl(arr):
    n = len(arr)
    largest = 0
    for i in range(n):
        if arr[i] > largest:
            largest = arr[i]
    return largest


"""Find the smallest element in the list"""

def MiniEl(arr):
    n = len(arr)
    smallest = arr[0]
    for i in range(n):
        if arr[i] < smallest:
            smallest = arr[i]
    return smallest


"""Find the second largest number in the list."""

def SecondLargest(arr):
    n = len(arr)
    largest = arr[0]

    for i in range(n):
        if largest < arr[i]:
            largest = arr[i]
    arr.remove(largest)
    secondLargest = arr[0]
    for i in range(len(arr)):
        if secondLargest < arr[i]:
            secondLargest = arr[i]
    return secondLargest


"""Print all the maxima’s in a list. (A value is a maximum if the value before and after its index are smaller than it is or does not exist.)"""


def Maxima(arr):
    maxArr = []
    n = len(arr)
    if n == 1:
        return arr[0]
    else:
        if (arr[0] > arr[1]):
            maxArr.append(0)

        for i in range(1, n -1 ):
            if (arr[i-1] < arr[i] > arr[i + 1]):
                maxArr.append(i)

        if ( arr[-1] > arr[-2]):
            maxArr.append(-1)

        return maxArr


print(Maxima(array))