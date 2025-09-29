import pytest
from lab4.task_1 import is_correct_parentheses

# 1. Правильная скобочная последовательность
def test_valid_simple():
    input_string = "()"
    result = is_correct_parentheses(input_string)
    assert result is True

# 2. Сложная сбалансированная структура
def test_valid_complex():
    input_string = "(((()())))"
    result = is_correct_parentheses(input_string)
    assert result is True

# 3. Несбалансировано — лишняя закрывающая
def test_unbalanced_extra_closing():
    input_string = "(()))"
    result = is_correct_parentheses(input_string)
    assert result is False

# 4. Несбалансировано — лишняя открывающая
def test_unbalanced_extra_opening():
    input_string = "((())"
    result = is_correct_parentheses(input_string)
    assert result is False

# 5. Неправильный порядок
def test_wrong_order():
    input_string = ")("
    result = is_correct_parentheses(input_string)
    assert result is False

# 6. Пустая строка (граничный случай)
def test_empty_string():
    input_string = ""
    result = is_correct_parentheses(input_string)
    assert result is True

# 7. Нет скобок, только текст
def test_no_parentheses_text_only():
    input_string = "abc"
    result = is_correct_parentheses(input_string)
    assert result is True

# 8. Только открывающие скобки
def test_only_opening():
    input_string = "(((("
    result = is_correct_parentheses(input_string)
    assert result is False

# 9. Только закрывающие скобки
def test_only_closing():
    input_string = "))))"
    result = is_correct_parentheses(input_string)
    assert result is False

# 10. Перемешано с другими символами
def test_mixed_with_text():
    input_string = "(abc(def)g)"
    result = is_correct_parentheses(input_string)
    assert result is True