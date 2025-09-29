import pytest
from lab1.task_1 import binary_search

# ТЕСТ 1: Успешный поиск элемента в середине
def test_search_middle():
    arr = [1, 2, 3, 4, 5]
    target = 3

    found, index, steps = binary_search(arr, target)

    assert found is True
    assert index == 2
    assert steps >= 1

# ТЕСТ 2: Успешный поиск первого элемента
def test_search_first_element():
    arr = [1, 2, 3, 4, 5]
    target = 1

    found, index, steps = binary_search(arr, target)

    assert found
    assert index == 0
    assert steps >= 1

# ТЕСТ 3: Успешный поиск последнего элемента
def test_search_last_element():
    arr = [1, 2, 3, 4, 5]
    target = 5

    found, index, steps = binary_search(arr, target)

    assert found
    assert index == 4

# ТЕСТ 4: Неуспешный поиск (элемент отсутствует)
def test_search_not_found():
    arr = [1, 2, 3, 4, 5]
    target = 10

    found, index, steps = binary_search(arr, target)

    assert not found
    assert index == -1

# ТЕСТ 5: Граничный случай — одиночный элемент (совпадает)
def test_one_element_found():
    arr = [42]
    target = 42

    found, index, steps = binary_search(arr, target)

    assert found
    assert index == 0

# ТЕСТ 6: Граничный случай — одиночный элемент (не совпадает)
def test_one_element_not_found():
    arr = [42]
    target = 10

    found, index, steps = binary_search(arr, target)

    assert not found
    assert index == -1

# ТЕСТ 7: Ошибочный случай — пустой список
def test_empty_list_raises():
    arr = []
    target = 5

    with pytest.raises(ValueError, match="Список не должен быть пустым"):
        binary_search(arr, target)

# ТЕСТ 8: Ошибочный случай — список не отсортирован
def test_not_sorted_list_raises():
    arr = [3, 2, 1]
    target = 2

    with pytest.raises(ValueError, match="Список должен быть отсортирован по возрастанию"):
        binary_search(arr, target)