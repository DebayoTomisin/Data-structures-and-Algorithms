"""In this chapter, we'll be considering hash table and their common use cases"""
"""A hash function is a function where you put in a string, string here means any kind of data, and you get 
back a number. We day that a hash function maps strings to numbers. Below are some requirements for a hash function
    1. It needs to be consistent. for example, suppose you out in apple, and get back 4, every time we put in apple
        we must get back 4.
    2. It should map different words to different numbers
"""

"""This is how the hash function works:
take for example, we try to store the prices of games, say FIFA, PES, COD and Cooking fever, we create an empty array
that is meant to store the prices of these goods, if we pass in the names of our games
    1. FiFA the hash function outputs 3
    2. PES the hash function outputs 1
    3. COD the hash function outputs 0
    4. Cooking fever, the hash function outputs 2"""


# Maximum sub array problem

def crossSubArray(arr, low, mid, high):
    sum = 0
    maxLeft = 0
    leftIndex = 0
    
    for i in range(low, mid):
        sum += arr[i]
        if sum >= maxLeft:
            maxLeft = sum
            leftIndex = i

    sum = 0
    maxRight = 0
    rightIndex = 0
    for j in range(mid + 1, high):
        sum += arr[j]
        if sum >= maxRight:
            maxRight = sum
            rightIndex = j

    return(leftIndex, rightIndex, maxLeft + maxRight)