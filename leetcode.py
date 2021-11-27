"""This is the file where I'll write all my leet code endeavours and solutions"""

"""Reverse the vowels of a string"""


def reverseVowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    string = list(string)
    index = []
    vowel = []
    for i in range(len(string)):
        if string[i] in vowels:
            vowel.append(string[i])
            index.append(i)
    vowel = vowel[::-1]
    final =[]
    ind = 0
    for i in range(len(string)):
        if i in index:
            final.append(vowel[ind])
            ind += 1
        else:
            final.append(string[i])
    return "".join(final)


print(reverseVowels('hello'))
print(reverseVowels('programming'))
