from abc import ABCMeta
from abc import abstractmethod
import  math
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


print(ListMethods.sumArray([1, 4, 5, 10, 8, 9]))
print(ListMethods.sequentialSearch([1, 4, 5, 9], 4))
print(ListMethods.binarySearch([1, 5, 6, 10, 17, 20, 26], 33))
print(ListMethods.rotateArray([1, 2, 3, 6, 7, 9, 10, 11, 34], 3))
print(ListMethods.reverseArray([1, 3, 4, 6, 8], 1, 3))
