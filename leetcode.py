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
