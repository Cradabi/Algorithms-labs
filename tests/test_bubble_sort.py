import pytest
from lab2.Task_2 import bubble_sort

# 1. Нормальный случай (корректный)
def test_unsorted_integers():
    arr = [5, 1, 4, 2, 8]
    result = bubble_sort(arr.copy())
    assert result == [1, 2, 4, 5, 8]

# 2. Уже отсортированный список
def test_sorted_list():
    arr = [1, 2, 3, 4, 5]
    result = bubble_sort(arr.copy())
    assert result == [1, 2, 3, 4, 5]

# 3. Обратный порядок
def test_reverse_sorted_list():
    arr = [5, 4, 3, 2, 1]
    result = bubble_sort(arr.copy())
    assert result == [1, 2, 3, 4, 5]

# 4. Повторяющиеся значения
def test_with_duplicates():
    arr = [4, 2, 2, 8, 3, 3, 1]
    result = bubble_sort(arr.copy())
    assert result == sorted(arr)

# 5. Все элементы одинаковые (крайний случай)
def test_all_same_elements():
    arr = [7, 7, 7, 7]
    result = bubble_sort(arr.copy())
    assert result == [7, 7, 7, 7]

# 6. Один элемент (граничный случай)
def test_single_element():
    arr = [42]
    result = bubble_sort(arr.copy())
    assert result == [42]

# 7. Пустой список (граничный случай)
def test_empty_list():
    arr = []
    result = bubble_sort(arr.copy())
    assert result == []

# 8. Отрицательные числа
def test_negative_numbers():
    arr = [0, -2, 5, -1, 3]
    result = bubble_sort(arr.copy())
    assert result == sorted(arr)

# 9. Смешанные типы: float + int
def test_floats_and_ints():
    arr = [3, 1.5, 2.2, 1, 0]
    result = bubble_sort(arr.copy())
    assert result == sorted(arr)