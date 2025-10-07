
n = int(input("введите гипероператор : "))
chislo = int(input('введите сам оператор : '))
def f(n):
    r = []
    t = chislo ** (chislo ** n)
    r.append(t)
    klin = r[0]
    pin = [int(y) for y in str(klin)]
    return len(pin)
print(f(n))