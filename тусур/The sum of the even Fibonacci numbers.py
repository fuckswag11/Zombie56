def s(l=4000000):
    a, b = 1, 2 
    t = 0
    
    while a <= l:
        if a % 2 == 0:
            t += a
        a, b = b, a + b
    
    return t

print(s())