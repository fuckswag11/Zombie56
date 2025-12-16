def move_zeros(lst):
    result = [x for x in lst if x != 0]
    result.extend([0] * (len(lst) - len(result)))
    return result

# Тестирование функции
assert move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]) == [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]
assert move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]) == [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Пример использования
print(move_zeros([1, 0, 1, 2, 0, 1, 3])) # [1, 1, 2, 1, 3, 0, 0]