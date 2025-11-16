def binary_search(arr: list, target: int | str) -> int:
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > target:
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            return mid 
    return None



arr = range(100)

print(binary_search(arr, 75))


# I have used three "if" statament in the first time, there are unnecessary comparasions using three "if"s