n = int(input(""))
k = int(input(""))

day = 1

for i in range(1, n):
    print("   ", end="")

i = n

while day <= k:
    if day <= 10:
        print(f' {day}', end="")
    else:
        print(f'{day}', end="")
    if i % 7 == 0 or day == k:
        print()
    else:
        print(" ", end="")
    day+=1 
    i+=1
    