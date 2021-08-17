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
    addL = 0
    maxLeft = 0
    leftIndex = 0
    
    for i in range(low, mid + 1):
        addL += arr[i]
        # print(addL)
        if addL > maxLeft:
            maxLeft = addL
            leftIndex = i
    print('the value of max left is', maxLeft)

    addR = 0
    maxRight = 0
    rightIndex = 0
    for j in range(mid + 1, high):
        print(j)
        addR += arr[j]
        # print(addR)
        if addR > maxRight:
            maxRight = addR
            rightIndex = j
    print('the maximum value in right is', maxRight)

    return leftIndex, rightIndex, maxLeft + maxRight


array = [1, -6, 2, 9, 12, -22, 4]
mid = int(0 + len(array) / 2)
print(crossSubArray(array, 0, mid, len(array)))
