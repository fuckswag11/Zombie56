def encode(message, key):
    slov = {}
    for i in range(len(key)):
        print(key[i + 1])
        value = key[i]
        slov[key] = key[i + 1]
        value = key[i + 1]
        slov[key] = key[i]
    return slov

print(encode("popopo", "po"))
    

# def decode(encrypted_message, key):
#     # Ваша реализация декодирования
#     pass
