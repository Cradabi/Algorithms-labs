def binary_search(arr, target):
    if not arr:
        raise ValueError("Список не должен быть пустым")

    low = 0
    high = len(arr) - 1
    steps = 0

    while low <= high:
        steps += 1
        mid = (low + high) // 2

        if arr[mid] == target:
            return True, mid, steps
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return False, -1, steps