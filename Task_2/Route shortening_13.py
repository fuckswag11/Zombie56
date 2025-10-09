def dirReduc(n):
    s = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}
    r = []
    for i in n:
        if r and r[-1] == s[i]: r.pop()
        else: r.append(i)
    return r
print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))

