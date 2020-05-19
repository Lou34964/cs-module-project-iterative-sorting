def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    # While we haven't narrowed it down to one element ...
    while low <= high:
        # ... check the middle element
        mid = (low + high) // 2
        guess = arr[mid]
        # Found the item.
        if guess == target:
            return mid
        # The guess was too high.
        if guess > target:
            high = mid - 1
        # The guess was too low.
        else:
            low = mid + 1

    return -1  # not found