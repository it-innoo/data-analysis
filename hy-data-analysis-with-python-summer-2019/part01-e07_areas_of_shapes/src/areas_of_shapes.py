#!/usr/bin/env python3

import math


def printArea(area):
    print("The area is {:6f}".format(area))


def rectangle():
    width = float(input("Give width of the rectangle: "))
    height = float(input("Give height of the rectangle: "))
    return width * height


def circle():
    radius = float(input("Give radius of the circle: "))
    return radius**2 * math.pi


def triangle():
    base = float(input("Give base of the triangle: "))
    height = float(input("Give height of the triangle: "))
    return base*height/2


def main():
    # enter you solution here
    shapes = {'t': 'triangle', 'r': 'rectangle', 'c': 'circle'}

    shape = input('Choose a shape ({t}, {r}, {c}); '.format(**shapes))
    while shape != "":
        if shape == 'triangle':
            printArea(triangle())
        elif shape == 'rectangle':
            printArea(rectangle())
        elif shape == 'circle':
            printArea(circle())
        elif shape == '':
            break
        else:
            print("Unknown shape!")
        shape = input('Choose a shape ({t}, {r}, {c}); '.format(**shapes))


if __name__ == "__main__":
    main()
