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


"""This problem suggests that we find if a string is a permutation of another string"""

NO_OF_CHARS = 256


def arePermutation(str1, str2):

    # Create a count array and initialize all
    # values as 0
    count = [0 for i in range(NO_OF_CHARS)]
    i = 0

    # For each character in input strings,
    # increment count in the corresponding
    # count array
    while str1[i] and str2[i]:

        count[str1[i]] += 1
        count[str2[i]] -= 1

    # If both strings are of different length.
    # Removing this condition  will make the
    # program fail for strings like "aaca" and
    # "aca"
    if str1[i] or str2[i]:
        return False

    # See if there is any non-zero value in
    # count array
    for i in range(NO_OF_CHARS):
        if count[i]:
            return False
    return True


print(arePermutation("string", "string"))
