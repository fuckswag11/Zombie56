def sqrt(n):
    return n ** 0.5
def log2(n):
    if n <= 0:
        raise ValueError
    import math
    return math.log(n) / math.log(2)
def factorial(n):
    if n < 0: return None 
    s = 1
    for i in range(1, n + 1):
        s *= i
    return s
def complexity_table(sizes):
    headers = [
        "n", "O(1)", "O(log n)", "O(sqrt(n))", "O(n)", "O(n log n)", "O(n^2)", "O(n^3)", "O(2^n)", "O(n!)"
    ]
    print("\t".join(headers))
    print("-" * (len(headers) * 12))
def complexity_table(sizes):
    headers = [
        "n", "O(1)", "O(log n)", "O(sqrt(n))", "O(n)", "O(n log n)", "O(n^2)", "O(n^3)", "O(2^n)", "O(n!)"
    ]
    print("\t".join(headers))
    print("-" * (len(headers) * 12))
    for n in sizes:
        if n <= 0:
            continue 
        o1 = 1
        ologn = log2(n)
        osqrt = sqrt(n)
        on = n
        onlogn = n * log2(n)
        on2 = n ** 2
        on3 = n ** 3
        try:
            o2n = 2 ** n
        except OverflowError:
            o2n = float('inf')
        try:
            onfact = factorial(n)
        except OverflowError:
            onfact = float('inf')
        r = [
            str(n),
            str(o1),
            f"{ologn:.2f}",
            f"{osqrt:.2f}",
            str(on),
            f"{onlogn:.2f}",
            str(on2),
            str(on3),
            f"{o2n:.2e}" if o2n != float('inf') else "inf",
            f"{onfact:.2e}" if onfact != float('inf') else "inf"
        ]
        print("\t".join(r))
print(complexity_table([1, 10, 100, 100]))