def f(d):
    n = 1
    while (10 ** n) % d != 1:
        n += 1
    return n
s = 0
k = 0
for d in range(2, 1000):
    if d % 2 != 0 and d % 5 != 0:
        k = f(d)
        if k > s: 
            s = k
            result_d = d
print(result_d)

