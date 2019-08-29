#!/usr/bin/env python3


def merge(L1, L2):
    L = []
    l = len(L1) + len(L2)
    l1 = len(L1)
    l2 = len(L2)
    i = j = 0

    while (i < l1) and (j < l2):
        if L1[i] < L2[j]:
            L.append(L1[i])
            i += 1
        else:
            L.append(L2[j])
            j += 1

    while i < l1:
        L.append(L1[i])
        i += 1

    while j < l2:
        L.append(L1[j])
        j += 1

    return L


def main():
    pass


if __name__ == "__main__":
    main()
