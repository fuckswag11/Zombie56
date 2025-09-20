def square_digits(s):
    x = []
    r = list(s)
    for i in r:
        i = int(i) ** 2
        x.append(i)
    s = ''.join(str(g) for g in x)
    return s
print(square_digits('9119'))    