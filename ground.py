from abc import ABCMeta
from abc import abstractmethod
import math
print('this is it gentlemen')
""" This is basically me brushing up on my python skills"""

class Shape(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, r=1):
        self.radius = r

    def setRadius(self, r):
        self.radius = r

    def area(self):
        return math.pi * math.pow(self.radius, 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class HelloWorld(object):
    @classmethod
    def main(cls, args):
        print('Hello World')


if __name__ == '__main__':
    import sys

    HelloWorld.main(sys.argv)


class ParameterPass:
    def __init__(self):
        A = [1, 2]
        self.Change(A)
        print(A)

    def Change(self, G):
        G.append(5)


class ListMethods(object):
    
    @classmethod
    def sumArray(cls, arr):
        size = len(arr)
        total = 0
        index = 0
        for i in range(size):
            total += total + arr[i]
            i += 1
        return total

    @classmethod
    def sequentialSearch(cls, arr, value):
        size = len(arr)
        for i in range(size):
            print(arr[i])
            if value == arr[i]:
                return True
            i += 1
        return False

    @classmethod
    def binarySearch(cls, arr, value):
        size = len(arr)
        low = 0
        high = size - 1
        while low <= high:
            mid = int((low + high) / 2)
            if arr[mid] == value:
                return 'Present'
            else:
                if arr[mid] < value:
                    low = mid + 1
                else:
                    high = mid - 1
        return 'not found'

    @classmethod
    def rotateArray(cls, arr, k):
        n = len(arr)
        cls.reverseArray(arr, 0, k-1)
        cls.reverseArray(arr, k, n-1)
        cls.reverseArray(arr, 0, n-1)
        return arr

    @classmethod
    def reverse(cls, arr, start, end):
        value = arr[start: end: -1]
        return value

    @classmethod
    def reverseArray(cls, arr, start, end):
        i = start
        j = end
        while i <= j:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i += 1
            j -= 1
        return arr

    @classmethod
    def maxSubArraySum(cls, arr):
        size = len(arr)
        maxSoFar = 0
        maxEndingHere = 0
        for i in range(size):
            maxEndingHere = maxEndingHere + arr[i]
            if maxEndingHere < 0:
                maxEndingHere = 0
            if maxSoFar < maxEndingHere:
                maxSoFar = maxEndingHere
            i += 1
        return maxSoFar


print(ListMethods.sumArray([1, 4, 5, 10, 8, 9]))
print(ListMethods.sequentialSearch([1, 4, 5, 9], 4))
print(ListMethods.binarySearch([1, 5, 6, 10, 17, 20, 26], 33))
print(ListMethods.rotateArray([1, 2, 3, 6, 7, 9, 10, 11, 34], 3))
print(ListMethods.rotateArray([1, 3, 4, 6, 8], 2))
print(ListMethods.maxSubArraySum([1, -6, -8, 10, 11, 21, -33]))


def insertionSort(arr):
    j = 0
    size = len(arr)

    for j in range(size):
        i = j - 1
        key = arr[j]
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key
    return arr


def insertionSortDecs(arr):
    j = 0
    size = len(arr)
    for j in range(size):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] < key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key
    return arr


def linearSearch(arr, value):
    size = len(arr)
    for i in range(size):
        if value == arr[i]:
            return i
    return -1


print(insertionSort([2, 1, 5, 3, 10, 22, 12, 11]))
# print(linearSearch([1, -5, 7, 21, 12, 5], 5))


def addSameIndex(arr1, arr2):
    newArr = []
    size1 = len(arr1)
    size2 = len(arr2)

    if size1 != size2:
        return newArr

    for i in range(size1):
        # result = 0
        result = arr1[i]
        for j in range(size2):
            if i == j:
                result += arr2[j]
        newArr.append(result)
    return newArr


print('Add of the same Index', addSameIndex([9, 2, 3], [4, 5, 6]))

k = [[1, 2, 3], [4, 5, 6]]
sumdata = []
for x in range(len(k[0])):
    z = 0
    for y in range(len(k)):
        z += k[y][x]
    sumdata.append(z)
# print(sumdata)
print(" ")
print(" ")

arr = [-100, 1, 5, 5, 9, 7, 6, -18, 2, -3]
for i in range(len(arr)):
    value = arr[i]
    ix = i
    for j in range(i+1, len(arr)):
        if arr[ix] > arr[j]:
            ix = j
    arr[i], arr[ix] = arr[ix], arr[i]

print(arr)


def selectionSort(arr):
    size = len(arr)
    for i in range(size):
        ix = i
        for j in range(i + 1, size):
            if arr[ix] > arr[j]:
                ix = j
        arr[i], arr[ix] = arr[ix], arr[i]
    return arr


print(' ')
print(selectionSort(arr))


"""What this problem is is that you find the number of values to the right of the set value that is less than the set
number. its a simple problem that i applied the idea of selection sort to solve. """


def getRightValue(arr):
    newArr = []
    for i in range(len(arr)):
        ix = i
        value = 0
        for j in range(ix + 1, len(arr)):
            if arr[ix] > arr[j]:
                value += 1
        newArr.append(value)
    return newArr


print(' ')


def mergeSort(arr):
    size = len(arr)
    p = 0
    q = int(size / 2)
    r = size
    L = arr[p:q]
    R = arr[q: r + 1]
    i = 0
    j = 0
    for k in range(p, r):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
    return arr


print(mergeSort([1, 2, 3, 4, 5, 6]))

arr2 = [1, 5, 8, 9, 14, 2, 3, 0]
size = len(arr2)
p = 0
q = int(size / 2)
r = size - 1
