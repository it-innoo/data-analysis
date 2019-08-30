#!/usr/bin/env python3


def distinct_characters(L):
    d = {}
    for l in L:
        s = l
        d[s] = len(set(s))

    return d


def main():
    print(distinct_characters(["check", "look", "try", "pop"]))


if __name__ == "__main__":
    main()
