# test_vowels.py
import pytest
from main import count_vowels

def test_only_vowels():
    """Тест строки, содержащей только гласные"""
    assert count_vowels('aeiou') == 5
    assert count_vowels('AEIOU') == 5
    assert count_vowels('aEiOu') == 5

def test_no_vowels():
    """Тест строки без гласных"""
    assert count_vowels('') == 0  # пустая строка
    assert count_vowels('bcdfgh') == 0
    assert count_vowels('BCDFGH') == 0
    assert count_vowels('123!@#') == 0

def test_mixed_string():
    """Тест смешанной строки с гласными и согласными"""
    assert count_vowels('Hello') == 2
    assert count_vowels('Python') == 1
    assert count_vowels('HELLO WORLD') == 3
    assert count_vowels('Hello World!') == 3
    assert count_vowels('aEiOu123bcd') == 5

def test_special_cases():
    """Тест особых случаев"""
    assert count_vowels(' ') == 0  # пробел
    assert count_vowels('12345') == 0  # только цифры
    assert count_vowels('!@#$%') == 0  # только спецсимволы