#Блочная сортировка
def block_sort(arr):
    # Находим минимум и максимум в массиве
    min_val = min(arr)
    max_val = max(arr)

    # Создаем пустые "ведра" (бакеты) для каждого элемента
    buckets = [[] for _ in range(min_val, max_val + 1)]

    # Распределяем элементы по соответствующим "ведрам"
    for num in arr:
        buckets[num - min_val].append(num)

    # Сортируем каждое "ведро" (если оно не пустое)
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(sorted(bucket))

    return sorted_array

# Пример использования
input_array = [4, 2, 7, 1, 9, 5, 3, 10, 6]
sorted_array = block_sort(input_array)
print("Отсортированный массив:", sorted_array)
