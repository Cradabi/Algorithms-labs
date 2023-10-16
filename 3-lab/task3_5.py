#Пирамидальная сортировка
def heapify(arr, n, i):
    largest = i  # Инициализируем наибольший элемент как корень дерева
    left = 2 * i + 1  # Индекс левого потомка
    right = 2 * i + 2  # Индекс правого потомка

    # Если левый потомок существует и больше корня
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Если правый потомок существует и больше корня
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Если наибольший элемент не корень
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Меняем корень и наибольший элемент
        # Рекурсивно применяем heapify к поддереву
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Строим максимальную кучу
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Извлекаем элементы из кучи по одному и добавляем их в отсортированный массив
    sorted_array = []
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Перемещаем текущий корень в конец
        sorted_array.append(arr.pop())  # Добавляем корень в отсортированный массив
        heapify(arr, i, 0)  # Вызываем heapify на уменьшенной куче

    sorted_array.append(arr[0])  # Добавляем последний элемент (корень) в отсортированный массив

    return sorted_array

# Пример использования
input_array = [11, 2, 7, 1, 9, 5, 3, 8, 6]
sorted_array = (heap_sort(input_array))
sorted_array.reverse()
print("Отсортированный массив:", sorted_array)