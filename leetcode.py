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


print('')
print(LongestSubStringkai("pwwkew"))
print('')
print(LongestSubStringSatou("abcabcbb"))
print('')


'''Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

It is guaranteed that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.'''


def ProductSubarray(array):
    hash = {}
    start = 0
    end = 1
    while end < len(array):
        product = array[start] * array[end]
        hash.update({product: [array[start], array[end]]})
        start += 1
        end += 1
    hashArray = list(hash.keys())
    hashArray = sorted(hashArray)

    return hashArray[-1]


print(ProductSubarray([-2,0,-1]))




