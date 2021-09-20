"""This chapter is about quick sort which uses divide and conquer algorithm"""

"""Note that quick sort is a lot faster than selection sort, it is a good example of elegant code.
Divide and conquer is a recursive algorithm, and is solved in two steps,
    1. Find the base case, this is should be the simplest possible case
    2. Divide and decrease the problem until it becomes the base case
According to divide and conquer with every recursive call, you have to reduce your problem.
Finding the base case seems to be the most important step, it involves finding the most basic form or the 
most basic way to solving the problem and then using that model in solving the entire problem"""

"Using an example, given an array of numbers, add up all the numbers and return the total"
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def sum_(arr):
    total = 0
    for x in arr:
        total += x
    return total


print(sum_(array))
"""To solve this same problem recursively, first thing to do is to figure out the base case, in this case
getting an array with one or zero elements is the base case, the next step is ensuring hat with every recursive call, 
we are closer to having an empty array"""


def sum_recursive(arr):
    total = 0
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + sum_recursive(arr[1:])


print(sum_recursive(array))

"""Write a recursive function to count the number of elements in a list"""


def count(arr):
    if not arr:
        return 0
    else:
        return 1 + count(arr[1:])


# print(count(array))


"""This is how quick sort works
we first select a pivot element, and then generate twi sub arrays, one sub array of elements less than the pivot and
another sub array of elements greater than the pivot etc and then we then combine the results to get a single sorted
array"""


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


array1 = [-3, 8, 10, 3, 21, 100, 2, 10, 4, 6, 33, 12, 1, 2, 0, -4, -6, 14, 14, -33, -45, 21, 101, 21, 23, 78, -2, -7]
print(quick_sort(array1))

"""the speed of quick sort is dependent on the pivot chosen"""


def multiplication(arr):
    total = []
    for i in range(len(arr)):
        total.append(arr[i] * arr[i:])
    return total


def multi(arr):
    if len(arr) < 2:
        for i in range(len(arr)):
            return [arr[i] * arr[i]]
    else:
        for i in range(len(arr)):
            return arr[i] * multi(arr[i+1:])


arr1 = [2, 3, 4, 5]
# print(multi(arr1))
# print(multiplication(array))


def quickSort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quickSort(less) + [pivot] + quickSort(greater)


Arr = [1, 9, 0, 7, 2, -3, 8, -11]
print(quickSort(Arr))


def binarySearch(arr, value):
    if len(arr) < 1:
        return []
    else:
        if len(arr) == 1:
            if value == arr[0]:
                return True
            else:
                return False
        high = len(arr) - 1
        low = 0
        mid = int(high / 2)
        return binarySearch(arr[low: mid], value)

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print('fibonacii')
print(fibonacci(1))


def powersof2(n):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    else:
        prev = powersof2(n / 2)
        curr = prev * 2
        return curr

print(powersof2(4))