def quicksort(array: list, left=0, right=None):
    if right is None:
        right = len(array) - 1
    if left < right:
        pivot = partition(array, left, right)
        quicksort(array, left, pivot-1)
        quicksort(array, pivot+1, right)

def partition(array, left, right):
    pivot = array[right]
    i = left - 1
    for j in range(left, right):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[right] = array[right], array[i+1]
    return i+1

########### 
a1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
a2 = [10, 7, 8, 9, 1, 5]
a3 = [5, 4, 3, 2, 1]

