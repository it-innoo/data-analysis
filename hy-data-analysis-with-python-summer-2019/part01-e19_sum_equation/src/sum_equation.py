#!/usr/bin/env python3


def sum_equation(L):
    if not L:
        return "0 = 0"

    result = list(map(str, L))
    return " + ".join(result) + f" = {sum(L)}"

    # My tryout version
    if len(L) == 0:
        return "0 = 0"

    from functools import reduce
    summa = reduce(lambda x, y: x+y, L, 0)
    S = []

    for i in L:
        S.append(str(i))

    result = " + ".join(S)
    result += " = " + str(summa)

    return result


def main():
    print(sum_equation([1, 5, 7]))


if __name__ == "__main__":
    main()
