from collections import Counter

"""The problem is to determine if a string is unique or not. This will be done using three approaches"""
# The hash table approach.


def UniqueStringHashTable(str):
    hashTable = {}
    for character in range(len(str)):
        if str[character] not in hashTable.keys():
            hashTable[str[character]] = 1
        else:
            return "String is not unique"
    return "String is unique"


# The ASCII representation method


def ASCIIUniqueString(str):

    if len(str) > 256:
        return "String is not unique"

    characterSet = [False] * 128

    for i in range(0, len(str)):
        value = ord(str[i])
        if characterSet[value]:
            return "String is not unique"

        characterSet[value] = True
    return "String is unique"


# The Method using python modules and packages that


def PythonPackageUniqueString(str):
    frequency = Counter(str)

    if len(frequency) == len(str):
        return "String is unique"
    else:
        return "String is not unique"


print(PythonPackageUniqueString("abbbh"))
