def is_anagram_method1(s1, s2):
    """
    Метод 1: Проверка вхождения (Метки)
    Идея: для каждого символа из s1 ищем совпадение в s2 и "помечаем" его.
    """
    r = []
    for i in s1:
        if i not in s2:
            return False
        elif i in s2:
            r.append(i)
    return True

def is_anagram_method2(s1, s2):
    """
    Метод 2: Сортировка и сравнение
    Идея: отсортировать обе строки и сравнить результаты.
    """
    s1 = sorted(s1)
    s2 = sorted(s2)
    if s1 == s2:
        return True
    else: return False

from itertools import *
def is_anagram_method3(s1, s2):
    """
    Метод 3: Полный перебор (brute force)
    Идея: сгенерировать все перестановки s1 и проверить, есть ли среди них s2.
    Внимание: этот метод крайне медленный — используйте только для коротких слов (длина ≤ 7).
    """
    if len(s1) <= 7 and len(s2) <= 7:
        if s2 in [''.join(i) for i in permutations(s1)]:
            return True
        else: return False
    else: None 
            
def is_anagram_method4(s1, s2):
    """
    Метод 4: Подсчёт частот символов
    Идея: подсчитать, сколько раз встречается каждая буква в обеих строках, и сравнить счётчики.
    Предполагается, что слова содержат только строчные латинские буквы.
    """
    if len(s1) != len(s2):
        return False
    for i in s1:
        if s1.count(i) == s2.count(i):
            return True
        else:
            return False

import random

def find_anagrams_for_random_word(method_func):

    dictionary = ['qwerty', 'ytrewq', 'matwas', 'opana', 'papados', 'batuev', 'uiuiuiui', 'lend', 'dnel']

    word = random.choice(dictionary)
    print(f"Исходное слово: {word}")
    
    anagrams = []
    for candidate in dictionary:
        if candidate != word and method_func(word, candidate):
            anagrams.append(candidate)
    
    print(f"Найдено анаграмм: {len(anagrams)}")
    print("Примеры:", anagrams[:10])
    return anagrams
    
# find_anagrams_for_random_word(is_anagram_method1)
# find_anagrams_for_random_word(is_anagram_method2)
# find_anagrams_for_random_word(is_anagram_method3)
find_anagrams_for_random_word(is_anagram_method4)

# print(is_anagram_method1('qwerty', 'qwerty'))
# print(is_anagram_method2('qwerty', 'qwerty'))
# print(is_anagram_method3('qwerty', 'qwerty'))
# print(is_anagram_method4('qwerty', 'qwerty'))
