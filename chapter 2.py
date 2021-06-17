"""This chapter covers the idea behind sorting
The trade off between arrays and linked list"""

# writing a function to find the smallest element in an array
# and then the selection sort algorithm which has a run time of O(n*2)


def find_Smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    f = 0
    for i in range(f, len(arr)):
        if arr[i] < arr[f]:
            smallest_index = i
        # print(f + i)
    return smallest_index


array = [1, 5, 0, 8, 7, -3, 77, -23, 9]
print('the smallest element in the array is set at index:', find_Smallest(array))


def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_Smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


print('The result of the selection sort algorithm is: ', selection_sort(array))

