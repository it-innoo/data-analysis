#!/usr/bin/env python3


def triple(x):
    "multiplies its parameter by three."
    return 3*x


def square(x):
    "raises its parameter to the power of two"
    return x**2


def main():

    for i in range(1, 11):
        s = square(i)
        t = triple(i)
        if s > t:
            break
        print("triple({})=={} square({})=={}"
              .format(i, t, i, s))


if __name__ == "__main__":
    main()
