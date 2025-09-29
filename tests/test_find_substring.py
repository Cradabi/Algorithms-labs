import pytest
from lab7.task1 import (
    find_most_frequent_substring,
    naive,
    kmp,
    rabin_karp,
    boyer_moore_horspool
)

# 1. Обычный случай: строка с разным количеством повторов
def test_most_frequent_simple():
    text = "12131415121312"  # 12 → 3 раза, 13 → 2, 14/15 → 1
    pattern, count = find_most_frequent_substring(text, naive)
    assert pattern == '12'
    assert count == 3


# 2. Строка слишком короткая (<2 символов)
def test_text_too_short():
    text = "1"
    pattern, count = find_most_frequent_substring(text, kmp)

    assert pattern in ['', None]
    assert count == 0


# 3. В строке нет двузначных чисел вообще (нет двух подряд цифр)
def test_no_digit_pairs_found():
    text = "abcxyzooo"
    pattern, count = find_most_frequent_substring(text, rabin_karp)

    assert pattern == ''
    assert count == 0


# 4. Несколько паттернов с одинаковой частотой
def test_multiple_equal_frequent_matches():
    text = "1213131213"  # 12 → 3, 13 → 3

    pattern, count = find_most_frequent_substring(text, boyer_moore_horspool)

    assert pattern in {'12', '13'}
    assert count == 3


# 5. Ограниченный диапазон поиска (start, end)
def test_custom_search_range():
    text = "12345678"  # двузначные: 12, 23, 34, ..., 78
    pattern, count = find_most_frequent_substring(text, naive, start=34, end=36)

    assert pattern == '34'
    assert count == 1


# 6. Проверка согласованности между всеми алгоритмами
@pytest.mark.parametrize("search_fn", [naive, kmp, rabin_karp, boyer_moore_horspool])
def test_consistency_across_algorithms(search_fn):
    text = "121212313131"  # 12: 3, 13: 3, 31: 2
    pattern, count = find_most_frequent_substring(text, search_fn)

    assert pattern in {'12', '13'}
    assert count == 3


# 7. Пустая строка
def test_empty_string():
    pattern, count = find_most_frequent_substring("", rabin_karp)

    assert pattern == ''
    assert count == 0


# 8. Один единственный двузначный паттерн
def test_single_occurrence():
    text = "random123number45inside78"  # '12' — 1 раз, '45' — 1, '78' — 1
    pattern, count = find_most_frequent_substring(text, naive)

    assert pattern in {'12', '45', '78'}
    assert count == 1


# 9. Граничный диапазон поиска — ничего не входит в диапазон
def test_range_excludes_all():
    text = "12131415"
    pattern, count = find_most_frequent_substring(text, naive, start=90, end=99)

    assert pattern == ''
    assert count == 0