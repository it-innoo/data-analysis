#!/usr/bin/env python3


def transform(s1, s2):

    result = zip(s1.split(), s2.split())
    resultList = list(result)
    c, v = zip(*resultList)
    c = list(map(int, c))
    v = list(map(int, v))

    L = [c * v for c, v in zip(c, v)]
    return L
    # return list(list(map(int, L)))


def main():
    L = transform("1 5 3", "2 6 -1")
    print(L)


if __name__ == "__main__":
    main()
