def factorial(n):
    if n < 0: return None
    if n == 0 or n == 1: return 1
    k = 1
    for i in range(1, n + 1):
        k *= i
    return k
print(factorial(5))