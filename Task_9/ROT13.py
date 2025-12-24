def rot13_0(text: str) -> str:
    arr = []
    for symbol in text:
            if ord(symbol) <= 109:
                arr.append(chr(ord(symbol) + 13))
            elif ord(symbol) >= 110:
                arr.append(chr(ord('a') + ((ord(symbol) + 13) - 123)))

    return ''.join(arr)

print(rot13_0("hello"))
print(rot13_0(rot13_0("hello")))
