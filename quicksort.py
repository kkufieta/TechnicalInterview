"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    start = 0
    end = len(array) - 1
    pivot = end
    while start < pivot:
        if array[start] >= array[pivot]:
            temp = array[pivot-1]
            array[pivot-1] = array[pivot]
            if start + 1 == pivot:
                array[pivot] = temp
            else:
                array[pivot] = array[start]
                array[start] = temp
            pivot -= 1
        else:
            start += 1
    if pivot > 0:
        left_array = quicksort(array[0:pivot])
    elif pivot == 0:
        left_array = []
    if pivot < end:
        right_array = quicksort(array[pivot+1:])
    elif pivot == end:
        right_array = []

    array = left_array + [array[pivot]] + right_array
    return array

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)

