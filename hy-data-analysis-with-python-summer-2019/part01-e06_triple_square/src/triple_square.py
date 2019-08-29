#!/usr/bin/env python3


def triple(x):
    "multiplies its parameter by three."
    return 3*x


def square(x):
    "raises its parameter to the power of two"
    return x**2


def main():

    for i in range(3, 11):
        if square(i) > triple(i):
            break
        print("triple({})=={} square({})=={}"
              .format(i, triple(i), i, square(i)))


if __name__ == "__main__":
    main()
