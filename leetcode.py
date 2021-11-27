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
