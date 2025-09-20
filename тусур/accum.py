def accum(s):
    f = []
    for i, i1 in enumerate(s):
        k = i1.upper() + i1.lower() * i
        f.append(k)
    return '-'.join(f)
print(accum("abcd"))      