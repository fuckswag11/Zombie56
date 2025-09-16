m = int(input('напишите месяц :'))
n = int(input('напишите год :'))
if m == 1 and 3 and 5 and 7 and 8 and 10 and 12:
    f = 31
    print(f'количесвто дне в месяце : {f}')
elif m == 4 and 6 and 9 and 11:
    f = 30
    print(f'количесвто дне в месяце : {f}')
elif m == 2 and n % 4 == 0:
    f = 29
    print(f'количесвто дне в месяце : {f}')
else: 
    f = 28
    print(f'количесвто дне в месяце : {f}')
    