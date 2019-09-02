#!/usr/bin/env python3


def is_positive(x):
    """Returns True if x is positive and False if x is a negative number"""
    return x > 0


def positive_list(L):
    return list(filter(is_positive, L))


def main():
    L = positive_list([2, -2, 0, 1, -7])
    print(L)


if __name__ == "__main__":
    main()
