#Сортировка слиянием
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Находим средний индекс массива
        left_half = arr[:mid]  # Разделяем массив на две половины
        right_half = arr[mid:]

        # Рекурсивно сортируем каждую из половин
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Слияние двух половин в отсортированный массив
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Проверяем, остались ли элементы в обеих половинах и добавляем их
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Пример использования
input_array = [4, 2, 7, 1, 9, 5, 3, 10, 6]
merge_sort(input_array)
print("Отсортированный массив:", input_array)
