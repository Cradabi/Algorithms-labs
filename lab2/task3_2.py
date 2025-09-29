def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

# Пример использования:
my_list = [12, 11, 13, 5, 6, 7]
sorted_list = quick_sort(my_list)
print("Отсортированный массив:", sorted_list)
