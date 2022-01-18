"""This is the file where I'll write all my leet code endeavours and solutions"""

"""Reverse the vowels of a string"""


def reverseVowels(string):
    vowels = 'aeiouAEIOU'

    v, k = [], [],
    string = list(string)
    for i in range(len(string)):
        if string[i] in vowels:
            v.append(string[i])
            k.append(i)
    v = v[::-1]  # this is the process of reversing the list
    for i in range(len(k)):
        string[k[i]] = v[i]
    return ''.join(string)


print(reverseVowels('hello'))
print(reverseVowels('programming'))

"""You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words"""


def GoodStrings(words, char):
    count = 0
    for word in words:
        if len(word) <= len(char):
            word = list(word)
            word_ = list(set(word))
            print(word_)
            x = True
            for letter in word_:
                if (letter not in char) or word.count(letter) > char.count(letter):
                    x = False
                    break
            if x:
                count += len(word)
    return count


def GoodStings_(words, chars):
    count = 0
    for i in words:
        if len(i) <= len(chars):
            l = list(i)
            l1 = list(set(l))
            x = True
            for k in l1:
                if (k not in chars) or (l.count(k) > chars.count(k)):
                    x = False
                    break

            if (x == True):
                count += len(i)
    return (count)


words = ["hello", "world", "leetcode"]
chars = "welldonehoneyr"

print('')

print(GoodStrings(words, chars))
print(GoodStings_(words, chars))
print('')

'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.'''


# this is the brute force approach to this problem

def SumTarget(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            sum_ = arr[i] + arr[j]
            if sum_ == target:
                return [i, j]
    return False


def SumTargetKai(arr, target):
    hash_table = {}

    for i in range(len(arr)):
        secondNumber = target - arr[i]
        if secondNumber in hash_table.keys():
            secondIndex = arr.index(secondNumber)
            if i != secondIndex:  # this is to make sure we are not using the same index
                return sorted([i, secondIndex])
        hash_table.update({arr[i]: i})
    return []


print(SumTargetKai([2, 7, 11, 15], 9))
print('')
print(SumTarget([2, 7, 11, 15], 22))

'''Longest Substring Without Repeating Characters'''


def LongestSubstring(string):
    hash = {}
    for i in range(len(string)):
        print(string[i])
        if string[i] in hash.keys():
            hash.update({string[i]: i})
            return len(hash.keys())
        hash.update({string[i]: i})
    return 0


def LongestSubStringSatou(string):
    subarray = []
    hash = {}
    for i in range(len(string)):
        if string[i] in hash.keys():
            length = len(hash.keys())
            subarray.append(length)
            hash.clear()
            hash.update({string[i]: i})
        else:
            hash.update({string[i]: i})
    return max(subarray)


def LongestSubStringkai(string):
    window = {}
    start = end = 0
    ans = 0

    for i in range(len(string)):
        if string[i] in window and window[string[i]] >= start:
            start = window[string[i]] + 1
        window[string[i]] = i
        end += 1
        ans = max(ans, end - start)
    return ans


print('the longest sub string problem')
print(LongestSubStringkai("pwwkew"))
print('')
print(LongestSubStringSatou("abcabcbb"))
print('')

'''Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

It is guaranteed that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.'''


def ProductSubarray(array):
    if len(array) == 1:
        return array[0]
    if len(array) < 1:
        return array

    hash = {}
    start = 0
    end = 1
    while end <= len(array):

        if end == len(array):
            product = array[end - 1]
            hash.update({product: [array[end - 1]]})
            end += 1
        else:
            product = array[start] * array[end]
            hash.update({product: [array[start], array[end]]})
            start += 1
            end += 1
    hashArray = list(hash.keys())
    hashArray = sorted(hashArray)

    return hashArray[-1]


print(ProductSubarray([0, 2]))


def ProductSubArrayKai(array):
    curMax, curMin = 1, 1
    res = array[0]

    for n in array:
        vals = (n, n * curMax, n * curMin)
        print(vals)
        curMax, curMin = max(vals), min(vals)
        print(curMax, curMin)
        res = max(res, curMax)
    return res


print('')
print(ProductSubArrayKai([-2, 3, -4]))

'''Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest 
sum and return its sum.'''


def SumSubArray(array):
    maxend, maxsofar = array[0], array[0]

    for num in array[1:]:
        if num < (maxend + num):
            maxend += num
        else:
            maxend = num

        if maxsofar < maxend:
            maxsofar = maxend
    return maxsofar


print('')
print(SumSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))


def PalindromeStr(string):
    if string == string[::-1]:
        return True
    else:
        return False


print(PalindromeStr('racecar'))


'''Longest Palindromic substring'''

def PalindromicSubString(string):
    result = ''
    resultLen = 0
    resR, resL = 0, 0

    for i in range(len(string)):
        # odd number length of string
        l, r = i, i
        while l >= 0 and r < len(string) and string[l] == string[r]:
            if (r -l + 1) > resultLen:
                resR = r
                resL = l + 1
            l -= 1
            r += 1
        result = string[resL: resR]
    return result

    #     # even number length of string
    #     l, r = i, i + 1
    #     while l >= 0 and r < len(string) and string[l] == string[r]:
    #         if (r - l + 1) > resultLen:
    #             resR = r
    #             resL = l + 1
    #         l -= 1
    #         r += 1
    #     result = string[resL: resR]
    # return result

print('')
print(PalindromicSubString('babad'))


"""Remove Duplicates from Sorted Array
This problem challenges you to remove duplicate values from an input array without using an external ds"""

def removeDuplicates(arr):
    k = 0
    for i in range(len(arr)):
        if arr[k] == arr[i]:
            pass
        else:
            arr[k + 1] = arr[i]
            k += 1
    return k + 1


print(removeDuplicates([1, 1, 2]))


"""Remove Element: This problem involves removing a given element from an array, it doesn't need to be  removed per say
but the element should not be in the final output of the said input array"""


def removeElement(arr, val):
    k = 0

    for i in range(len(arr)):
        if arr[i] != val:
           arr[k] = arr[i]
           k += 1
    return k


print('')
print(removeElement([3, 2, 2, 3], 3))
