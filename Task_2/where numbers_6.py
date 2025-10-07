def f(k):
    k1 = k + 1
    for n in range(1, 10000):
        g11 = str(n * k)
        g22 = str(n * k1)
        if sorted(g11) == sorted(g22):
            return n 
print(f(325))