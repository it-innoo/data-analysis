#!/usr/bin/env python3


def detect_ranges(L):
    S = sorted(L)

    length = len(S)
    i = 0

    while i < length:
        i += 1

    return S


def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)


if __name__ == "__main__":
    main()
