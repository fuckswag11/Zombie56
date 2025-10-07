def is_anagram_method1(s1, s2):
    """
    Метод 1: Проверка вхождения (Метки)
    Идея: для каждого символа из s1 ищем совпадение в s2 и "помечаем" его.
    """
    r = []
    for i in list(s1):
        if i in list(s2):
            i.append(r)
    pass
def is_anagram_method2(s1, s2):
    """
    Метод 2: Сортировка и сравнение
    Идея: отсортировать обе строки и сравнить результаты.
    """
    s1 = ''.join(sorted(s1))
    s2 = ''.join(sorted(s2))
    if s1 == s2: True
    else: False
    pass
def is_anagram_method3(s1, s2):
    """
    Метод 3: Полный перебор (brute force)
    Идея: сгенерировать все перестановки s1 и проверить, есть ли среди них s2.
    Внимание: этот метод крайне медленный — используйте только для коротких слов (длина ≤ 7).
    """
    if len(s1) < 7:
        from itertools import permutations
        for i in s1:
            d = permutations(s1, repeat=len(s1))
            if d == s2:
                True
    pass
def is_anagram_method4(s1, s2):
    """
    Метод 4: Подсчёт частот символов
    Идея: подсчитать, сколько раз встречается каждая буква в обеих строках, и сравнить счётчики.
    Предполагается, что слова содержат только строчные латинские буквы.
    """
    q = {}
    for i in s1:
        if i in q:
            q[i] += 1
        else:
            q[i] = 1
    q2 = {}
    for i2 in s2:
        if i2 in q:
            q[i2] += 1
        else:
            q[i2] = 1
    q = q.sorted()
    q2 = q2.sorted()
    if q == q2:
        True
    else: False
    pass
import random

def find_anagrams_for_random_word(method_func):
    dictionry = open('dictionary.txt')
    word = random.choice(dictionary)
    print(f"Исходное слово: {word}")
    
    anagrams = []
    for candidate in dictionary:
        if candidate != word and method_func(word, candidate):
            anagrams.append(candidate)
    
    print(f"Найдено анаграмм: {len(anagrams)}")
    print("Примеры:", anagrams[:10])
    return anagrams
    

find_anagrams_for_random_word(is_anagram_method1)
find_anagrams_for_random_word(is_anagram_method2)
find_anagrams_for_random_word(is_anagram_method3)
find_anagrams_for_random_word(is_anagram_method4)