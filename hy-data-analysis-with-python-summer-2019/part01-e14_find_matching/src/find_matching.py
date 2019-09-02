#!/usr/bin/env python3


def find_matching(L, pattern):
    R = []

    for i, x in enumerate(L):
        if pattern in x:
            R.append(i)

    return R


def main():
    m = find_matching(["sensitive", "engine", "rubbish", "comment"], "en")
    print(m)


if __name__ == "__main__":
    main()
