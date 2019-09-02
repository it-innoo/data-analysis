#!/usr/bin/env python3


def reverse_dictionary(d):
    inv = {}

    for key in d:
        for value in d[key]:
            if value in inv.keys():
                values = inv.get(value)
                values.append(key)
            else:
                inv[value] = [key]
    return inv


def main():
    d = {
        'move': ['liikuttaa'],
        'hide': ['piilottaa', 'salata'],
        'six': ['kuusi'],
        'fir': ['kuusi']
    }
    print(d)
    inv = reverse_dictionary(d)
    print("===")
    print(inv)


if __name__ == "__main__":
    main()
