import pytest
from lab5.Task_1 import simulate_heist

# 1. Базовый случай: можно украсть все предметы за 1 заход
def test_success_one_round():
    # Arrange
    w = [1, 2, 3]
    v = [10, 20, 30]
    scap = 10
    howm = 3
    runs = 1
    result = simulate_heist(w, v, scap, howm, runs)
    assert result["success"]
    assert result["total_items_stolen"] == 3
    assert result["total_value_stolen"] == 60
    assert result["rounds"] == 1


# 2. Недостаточно объема рюкзака для 1 предмета
def test_ransack_fails_capacity_too_small():
    w = [5, 6]
    v = [10, 20]
    scap = 3
    howm = 1
    runs = 3

    result = simulate_heist(w, v, scap, howm, runs)

    assert not result["success"]
    assert result["total_items_stolen"] == 0


# 3. Недостаточно попыток (заходов) чтобы украсть howm
def test_fail_due_to_insufficient_attempts():
    w = [1, 1, 1, 1, 1]
    v = [1, 1, 1, 1, 1]
    scap = 1
    howm = 5
    runs = 3

    result = simulate_heist(w, v, scap, howm, runs)

    assert not result["success"]
    assert result["total_items_stolen"] == 3  # максимум за 3 захода


# 4. Успешная кража в последнем заходе
def test_success_on_last_attempt():
    w = [1, 1, 1]
    v = [1, 1, 1]
    scap = 1
    howm = 3
    runs = 3

    result = simulate_heist(w, v, scap, howm, runs)

    assert result["success"]
    assert result["rounds"] == 3
    assert result["total_items_stolen"] == 3


# 5. Предметов больше, чем нужно украсть
def test_steals_only_needed_items():
    w = [1] * 10
    v = [1] * 10
    scap = 2
    howm = 5
    runs = 5

    result = simulate_heist(w, v, scap, howm, runs)

    assert result["success"]
    assert result["total_items_stolen"] >= 5
    assert result["rounds"] <= 5


# 6. Предметы с разным весом/ценностью
def test_prefer_more_valuable_items():
    w = [1, 3, 2]
    v = [5, 10, 4]  # Лучше 3+1 с ценностью 10+5
    scap = 4
    howm = 2
    runs = 1

    result = simulate_heist(w, v, scap, howm, runs)

    assert result["success"]
    assert result["total_value_stolen"] == 15
    assert sorted(result["items_per_round"][0]) == [0, 1]  # индексы 1 и 0

# 7. Граничный случай: howm = 0 (успех без кражи)
def test_zero_items_needed():
    w = [10, 20]
    v = [20, 30]
    scap = 5
    howm = 0
    runs = 1

    result = simulate_heist(w, v, scap, howm, runs)

    assert result["success"]
    assert result["total_items_stolen"] == 0
    assert result["total_value_stolen"] == 0


# 8. Граничный случай: пустые списки входных данных
def test_empty_inputs():
    w = []
    v = []
    scap = 10
    howm = 1
    runs = 1

    result = simulate_heist(w, v, scap, howm, runs)

    assert not result["success"]
    assert result["total_items_stolen"] == 0