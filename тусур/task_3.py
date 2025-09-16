n = list([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

s = int(input('ввиди число от 0 до 9 :'))
if 0 <= s < 10:
    for i in n:
        print(f"{s} на {i} = {s * i}")
else:
    print('error')
    
    