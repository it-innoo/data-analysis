#!/usr/bin/env python3

import math


def solve_quadratic(a, b, c):
    first = second = float(0)
    d = b**2 - (4*a*c)

    if d < 0:
        first = second = float(0)
    elif d == 0:
        first = second = (-b) / 2*a
    else:
        d = math.sqrt(d)
        first = ((-b) + d) / (2*a)
        second = ((-b) - d) / (2*a)

    return (first, second)


def main():
    print(solve_quadratic(1, -3, 2))
    print(solve_quadratic(1, 2, 1))
    print(solve_quadratic(-2, 2, 1))
    print(solve_quadratic(16, 24, 9))


if __name__ == "__main__":
    main()
