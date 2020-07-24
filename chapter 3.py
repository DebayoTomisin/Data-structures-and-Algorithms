"""This chapter explores the concept of recursion and how it applies in building algorithms"""

# let us do a quick recap of what we have learn't so far


def countdown(i):  # countdown 
    print(i)
    if i <= 0:
        return
    else:
        countdown(i - 1)


# print(countdown(10))

"""The call stack is basically used to save the variables from multiple function calls
the base function is called first, and when the other functions are called, they are placed on top of the stack 
and the base function is in a partially completed state, once the called functions are completed, they are then removed
from the stack"""

"""Call stacks also apply to recursive functions too"""

""""Using recursive stacks also comes at a cost, the cost is memory and basically takes a lot of memory, and in a case
where this happens you can either re write the code to use a loop or use tail recursion (but it is only supported
by some languages)"""


def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)


# print(factorial(10))


# EXERCISES

"""Write a python program to calculate the sum of a list of numbers"""


def sum_list(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + sum_list(arr[1:])


array = [1, 3, 4, 5, 6, 7, 8]
# print(sum_list(array))


"""Write a function that converts an integer to any string in any base """


def to_base(n, base):

    convert_string = "0123456789ABCEDF"
    if n < base:
        return convert_string[n]
    else:
        return to_base(n // base, base) + convert_string[n % base]


print(to_base(12, 16))

"""Recursive list sum"""


def recursive_list(arr):
    total = 0
    for element in arr:
        if type(element) == list:
            total = total + recursive_list(element)
        else:
            total = total + element
    return total


array1 = [1, 2, 3, [3, 4], [3, 6], 9]

print(recursive_list(array1))


