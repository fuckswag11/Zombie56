def b(n): return n * 1024
def kb(n): return n // 1024
m = int(input('введите число :'))
n = int(input('из килобайт в байты : напишите 2 \n' 'из байт в килобайты : напишите 3 : '))
if n == 2:
    f = b(m)
    print(f'вашы килобайты в байтах : {f}')
elif n == 3:
    f = kb(m)
    print(f'вашы байты в килобатах : {f}')
else: print('error')