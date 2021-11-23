import math
from io import StringIO

"""Here I'll be tackling all the exercise questions from Problem solving in DS and Algorithms  chapter 1"""
array = [1, 9, -5, 0, 12, 4]
array2 = [[1, 4, 6], [2, 3, -8, 1]]
array0 = [1, 0, 1, 0, 1, 1, 0, 0]
array3 = [1, 2, 0, 2, 1, 2, 0, 1, 1, 2, 1, 0]
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

        for i in range(1, n - 1):
            if (arr[i - 1] < arr[i] > arr[i + 1]):
                maxArr.append(i)

        if (arr[-1] > arr[-2]):
            maxArr.append(-1)

        return maxArr


print(Maxima(array))

"""Given a list with value 0 or 1, write a program to segregate 0 on the left side and 1 on the right side."""


def selection_sort(arr):
    size = len(arr)
    for i in range(size):
        ix = i
        for j in range(i + 1, size):
            if arr[ix] > arr[j]:
                ix = j
        arr[i], arr[ix] = arr[ix], arr[i]
    return arr


"""Reverse a list in-place. (You cannot use any additional list in other words Space Complexity should be O(1). )"""


def reverseOrder(arr):
    start = 0
    end = len(arr) - 1
    while start <= end:
        i = arr[start]
        ix = arr[end]
        arr[start] = ix
        arr[end] = i
        start += 1
        end -= 1
    return arr


"""Given a list of 0s and 1s. We need to sort it so that all the 0s are before all the 1s. in O(1) time"""


def sortBinary(arr):
    start = 0
    end = len(arr) - 1
    while start <= end:
        if arr[start] == 1 and arr[end] == 0:
            i = arr[start]
            ix = arr[end]
            arr[start] = ix
            arr[end] = i
            end -= 1
        start += 1
    return arr


"""Sorting to base 2"""


def base2Sort(arr):
    start = 0
    end = len(arr) - 1

    while start <= end:
        if (arr[start] == 2 or arr[start] == 1) and arr[end] == 0:
            i = arr[start]
            ix = arr[end]
            arr[start] = ix
            arr[end] = i
            start += 1
        # if arr[start] == 2 and arr[end] == 1:
        #     j = arr[start]
        #     jx = arr[end]
        #     arr[start] = jx
        #     arr[end] = j

        end -= 1
    return arr


"""Find the duplicate elements in a list of size n where each element is in the range 0 to n-1."""


def duplicateElements(arr):  # approach one
    size = len(arr)
    duplicates = []
    for i in range(size):
        for j in range(i + 1, size):
            if arr[i] == arr[j]:
                duplicates.append(arr[i])
    return duplicates


def duplicateTwo(arr):
    hash = {}
    for x in arr:
        if x != hash.keys():
            hash[x] = 1
        else:
            hash[x] += 1
    return hash


def duplicateThree(arr):
    for i in range(len(arr)):
        array[i] = 0
    for j in range(len(arr)):
        array[j] += 1


# print(duplicateThree([2, 7, 2, 3, 18, 6]))


"""Find the maximum element in a sorted and rotated list."""
rotated = [33, 30, 28, 22, 19, 15, 8, 6, 2]
low = 0
high = len(rotated)


def MaximRotatedList(arr, low, high, value):
    if len(arr) > 2:
        if high >= low:
            mid = int((high + low) / 2)
            if arr[mid] > value:
                value = arr[mid]
                return MaximRotatedList(arr, mid, high, value)
            elif arr[mid] < value:
                return MaximRotatedList(arr, low, mid, value)
    else:
        return arr[0]


def MaximRotatedListBrute(arr):
    maxim = 0
    for i in range(0, len(arr) - 1):
        if arr[i] > maxim:
            maxim = arr[i]
    return maxim


# print(MaximRotatedList(rotated))


'''The following are questions from the array and string chapter of cracking the coding interview'''

"""A string has unique values"""
strone = 'abba'


def uniqueStr(string):
    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            if string[i] == string[j]:
                return 'String is not unique'
    return 'string is unique'


# print(uniqueStr(strone))


def optimizedStr(string):
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            return 'String is not unique'
    return 'string is unique'


print('')
# print(optimizedStr(strone))
print('')

'''Given 2 strings, decide if one is a permutation of the other'''
string1 = 'dog'
string2 = 'G o d '


def PermutationStr(str1, str2):
    sorted1 = ''.join(sorted(str1))
    sorted2 = ''.join(sorted(str2))

    if len(sorted1) != len(sorted2):
        return False

    for i in range(len(sorted1)):
        if sorted1[i] == sorted2[i]:
            return True
        else:
            return False


print(PermutationStr(string1, string2))

'''Write a method to replace all spaces in a string with '%20'.'''


def StrReplacement(string):
    for i in range(len(string)):
        if string[i] == ' ':
            string = string.replace(string[i], '%20')
    return string


print('')
print(StrReplacement(string1))
print('')
print(StrReplacement(string2))

print('')


def removeDuplicates(arr):
    for i in range(len(arr) - 1):
        if (arr[i] == arr[i + 1]) and (arr[i] != '-'):
            arr[i + 1] = '-'

        if arr[i] == '-':
            arr += [arr.pop(i)]
    return arr


test_arr = [1, 1, 2, 4, 8, 8]
print(removeDuplicates(test_arr))


'''Given a string, write a function to check if it is a permutation of a palindrome'''


def PalindromePermutation(string):
    hashtable = {}
    count = 0
    for i in range(len(string)):
        if string[i] not in hashtable.keys():
            hashtable[string[i]] = 1
        else:
            hashtable[string[i]] += 1
    for item in hashtable.values():
        if item % 2 == 1:
            count += 1
    if count > 1:
        return False
    else:
        return True


print(' ')
# print(PalindromePermutation('racecar'))

print('')


'''There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.'''


def EditChecker(item1, item2):
    if item1 == item2:
        return True

    replace_count = 0
    if len(item1) == len(item2):
        for i in range(len(item1)):
            if item1[i] != item2[i]:
                replace_count += 1
        if replace_count >= 2:
            return False
        return True

    length1 = len(item1)
    length2 = len(item2)

    if abs(length1 - length2 > 1):
        return False
    index1 = 0
    index2 = 0
    while index1 < length1 and index2 < length2:
        if item1[index1] != item2[index2]:
            if index1 != index2:
                return False

            if length2 > length1:
                index2 += 1
            else:
                index1 += 1
        else:
            index2 += 1
            index1 += 1
    return True


print('')
print(EditChecker('aplee', 'apled'))


'''You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.'''


def MaximumProft2(arr):
    maxprofit = 0
    for i in range(len(arr) - 1):
        if arr[i + 1] > arr[i]:
            maxprofit += arr[i + 1] - arr[i]
    return maxprofit


print('')
print(MaximumProft2([7, 1, 5, 3, 6, 4]))


'''You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 '''
def MaximumProfit1(arr):
    highest = 0
    for i in range(len(arr) - 1):
        for j in range(i, len(arr)):
            current = arr[j] - arr[i]
            if current > highest:
                highest = current
    return highest


def optimizedProfit1(arr):
    minprice = arr[0]
    maxprofit = 0
    for i in range(len(arr)):
        if arr[i] < minprice:
            minprice = arr[i]
        elif arr[i] - minprice > maxprofit:
            maxprofit = arr[i] - minprice
    return maxprofit


print('')
print(optimizedProfit1([1, 2]))
print('')
print(MaximumProfit1([7, 1, 5, 3, 6, 4]))


'''Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3'''

def RepeatedString(string):
    compressed = ''
    count = 0
    n = len(string)
    for i in range(len(string) - 1):
        count += 1
        if string[i] != string[i + 1] or i == n:
            compressed += (string[i])
            compressed += (str(count))
            count = 0
    if len(compressed) > len(string):
        return string
    return compressed


print('')
print('this is the solution for compressed strings')
print('')
print(RepeatedString('aabcccccaaa '))