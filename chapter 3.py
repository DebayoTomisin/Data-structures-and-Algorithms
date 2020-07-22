"""This chapter explores the concept of recursion and how it applies in building algorithms"""

# let us do a quick recap of what we have learn't so far


def countdown(i):  # countdown 
    print(i)
    if i <= 0:
        return
    else:
        countdown(i - 1)


print(countdown(10))
