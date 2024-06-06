import csv
import sys


def apply_changes(data, changes):
    for change in changes:
        try:
            col, row, value = change.split(',')
            row, col = int(row), int(col)
            if row >= len(data) or col >= len(data[row]):
                print(f"Zmiana {change} wychodzi poza wykres (wiersz: {row}, kolumna: {col}). Pomijanie zmiany.")
                continue
            data[row][col] = value
        except ValueError:
            print(f"Zmiana {change} nie jest dobrze sformatowana. Pomijanie zmiany.")
    return data


def read_csv(file_path):
    with open(file_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data


def write_csv(file_path, data):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)


def display_csv(data):
    for row in data:
        print(','.join(row))


def main():
    if len(sys.argv) < 4:
        print("Dzialanie: python reader.py <plik_wejsciowy> <plik_wyjsciowy> <zmiana_1> <zmiana_2> ... <zmiana_n>")
        return

    file_in = sys.argv[1]
    file_out = sys.argv[2]
    changes = sys.argv[3:]

    data = read_csv(file_in)
    modified_data = apply_changes(data, changes)

    print("Zmodyfikowano zawartosc CSV: ")
    display_csv(modified_data)

    write_csv(file_out, modified_data)
    print(f"Zmodywikowana zawartosc CSV zapisuje do {file_out}")


if __name__ == "__main__":
    main()
