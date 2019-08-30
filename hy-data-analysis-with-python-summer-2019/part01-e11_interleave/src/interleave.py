#!/usr/bin/env python3

import itertools


def interleave(*lists):
    L = zip(*lists)
    return list(itertools.chain(*L))


def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))


if __name__ == "__main__":
    main()
