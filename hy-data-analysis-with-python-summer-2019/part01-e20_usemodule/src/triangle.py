# Enter you module contents here

"""This is the form of a docstring.

It can be spread over several lines.

"""

__author__ = "jukka"
__version__ = "0.0.1"

import math


def area(a, b):
    '''Returns triangle area.'''
    return a*b/2


def hypothenuse(a, b):
    '''Returns triangle hypothenus.'''
    return math.sqrt(a**2 + b**2)
