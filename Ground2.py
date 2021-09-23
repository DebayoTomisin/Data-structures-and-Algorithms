import math
matrix_a = [[2, 4, 1], [1, 1, 1]]
matrix_b = [[1, 2, 1], [1, 1, 1]]
n = len(matrix_a)
"""The Below is the brute force approach to multiplying square matrices."""
print(matrix_a)
lenA = len(matrix_a[0])
print(" ")
lenB = len(matrix_b[0])


"""This is the brute force approach to solving maximum sub array problem"""


def maxSubArray(arr):
    size = len(arr)
    maxSoFar = 0
    maxEndingHere = 0
    i = 0
    for i in range(size):
        maxEndingHere += arr[i]
        if maxEndingHere < 0:
            maxEndingHere = 0
        if maxSoFar < maxEndingHere:
            maxSoFar = maxEndingHere

    return maxSoFar


arr = [1, -6, 8, 9, 1]
print(maxSubArray(arr))

"""The divide and conquer approach to this problem"""

def CrossingSubArray(arr, low, mid, high):
    maxLeft = 0
    sumL = 0
    maxLeftIndex = 0

    for i in range(0, mid + 1):
        sumL += arr[i]

        if sumL >= maxLeft:
            maxLeft += sumL
            maxLeftIndex = i

    maxRight = 0
    sumR = 0
    maxRightIndex = 0

    for j in range(mid + 1, high):
        sumR += arr[j]

        if sumR >= maxRight:
            maxRight += sumR
            maxRightIndex = j

    return maxLeftIndex, maxRightIndex, maxLeft + maxRight


def MaximumSubArray(arr, low, high):
    if len(arr) < 2:
        return low, high, arr[low]
    elif len(arr) == 0:
        return 'Array is empty'
    else:
        mid = int(high / 2)
        leftLowIndex, leftHighIndex, leftSum = MaximumSubArray(arr, low, mid + 1)
        rightLowIndex, rightHighIndex, rightSum = MaximumSubArray(arr, mid + 1, high - 1)
        crossLowIndex, crossHighIndex, crossSum = CrossingSubArray(arr, low, mid, high)




arr1 = [4]
print(MaximumSubArray(arr1, 0, len(arr1)))


def factorial(n):
    if n < 1:
        return 1
    else:
        return n * factorial(n - 1)



def sumDigits(n):
    sum = 0
    while(n < 0):
        sum += n % 10
        n /= 10
    return sum

print(sumDigits(-1))

def binarySearch(arr, low, high, value):
    if high >= low:
        mid = int((high + low )/ 2)
        if arr[mid] == value:
            return True
        elif arr[mid] > value:
            return binarySearch(arr, low, mid - 1, value)
        else:
            return binarySearch(arr, mid + 1, high, value)
    else:
        return -1


print(binarySearch([0, 3, 6, 9, 10, 22], 0, 5, 22))


def recursiveSearch(arr, low, high, value):
    if high >= low:

        mid = int((low + high) / 2)
        if arr[mid] == value:
            return True, mid
        elif arr[mid] > value:
            return binarySearch(arr, low, mid - 1, value)
        else:
            return binarySearch(arr, mid + 1, high, value)
    else:
        return -1


"""Print all positive integer solutions to the equation a3 + b3 and d are integers between 1 and 1000."""


def brutePositive():
    n = 1000
    for a in range(1, n):
        for b in range(1, n):
            for c in range(1, n):
                for d in range(1, n):
                    if a**3 + b**3 == c**3 + d**3:
                        print(a, b, c, d)


def slightlyOptimized():
    n = 1000
    for a in range(1, n):
        for b in range(1, n):
            for c in range(1, n):
                d = math.pow(a**3 + b**3 + c**3, 1/3)
                if a ** 3 + b ** 3 == c ** 3 + d ** 3:
                    print(a, b, c, d)


slightlyOptimized()