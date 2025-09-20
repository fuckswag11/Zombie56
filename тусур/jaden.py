def to_jaden_case(string):
    r = string.split()
    return ' '.join(w.capitalize() for w in r)
print(to_jaden_case('I watch Twilight every night'))  