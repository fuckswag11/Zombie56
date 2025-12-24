def rot13_0(text: str) -> str:
    arr = []
    for i in text:
        s = ord(i)
        arr.append(chr(s + 3))
    print(''.join(arr))

def rot13_1(text: str) -> str:
    arr = []
    for i in text:
        s = ord(i)
        arr.append(chr(s - 3))
    print("", ''.join(arr))

print(rot13_0("abc"))
print(rot13_1("def"))

    

