def find_quirky_numbers(digit_count): 
    r = []
    if digit_count == 2:
        for i in range(0, 100):
            if (i // 10 + i % 10) ** 2 == i:
                r.append(str(i).zfill(2))
    if digit_count == 4:
        for i in range(0, 10000):
            k4 = str(i).zfill(4)
            k12 = str(k4)[0:2]
            k3 = str(k4)[2:4]
            if (int(k12) + int(k3)) ** 2 == i:
                r.append(k4)
    if digit_count == 6:
        for i in range(0, 1000000):
            k6 = str(i).zfill(6)
            k12 = str(k6)[0:3]
            k3 = str(k6)[3:6]
            if (int(k12) + int(k3)) ** 2 == i:
                r.append(k6)
    if digit_count == 8:
        for i in range(0, 100000000):
            k8 = str(i).zfill(8)
            k12 = str(k8)[0:4]
            k3 = str(k8)[4:8]
            if (int(k12) + int(k3)) ** 2 == i:
                r.append(k8)
    return r
   
# Тесты
def test_find_quirky_numbers():
    # Тест 1
    digit_count = 2
    expected_output = ['00', '01', '81']
    assert find_quirky_numbers(digit_count) == expected_output

    # Тест 2
    digit_count = 4
    expected_output = ['0000', '0001', '2025', '3025', '9801' ]
    assert find_quirky_numbers(digit_count) == expected_output

    # Тест 3
    digit_count = 6
    expected_output = ['000000', '000001', '088209', '494209', '998001']
    assert find_quirky_numbers(digit_count) == expected_output

    # Тест 4
    digit_count = 8
    expected_output = ['00000000', '00000001', '04941729', '07441984', '24502500', 
                       '25502500', '52881984', '60481729', '99980001'] 
    assert find_quirky_numbers(digit_count) == expected_output

    print("OK!")

# Запустите тесты
test_find_quirky_numbers()