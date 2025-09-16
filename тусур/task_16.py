n = int(input())
a = list(map(int, input().split()))
b = [0] * (n + 1)  # индексация с 1

for k in range(1, n + 1):
    place = a[k - 1]
    b[place] = k

print(' '.join(str(b[i]) for i in range(1, n + 1)))
