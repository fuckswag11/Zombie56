def f(n, k):
    cnt = 0 
    f = k
    while n >= f:
        cnt += n // f
        f *= k
    return cnt
print(f(10,2)) 
