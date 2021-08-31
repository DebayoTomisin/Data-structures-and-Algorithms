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