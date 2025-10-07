def parse_iban_lengths(filename):
    iban_lengths = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) == 2:
                    country_code = parts[0]
                    length = int(parts[1])
                    iban_lengths[country_code] = length
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
    except ValueError:
        print("Ошибка в данных файла.")
    return iban_lengths
if __name__ == "__main__":
    lengths = parse_iban_lengths('IBAN.txt')
    print(lengths)


