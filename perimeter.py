import math
"""
A module to compute perimeter of shapes
"""

def circle(rad: float) -> float:
    """
    Function to compute circle perimeter
    :param rad: Value of circle radius
    :return: Perimeter of circle
    """
    return rad * 2 * math.pi


def rectangle(side1: float, side2: float) -> float:
    """
    Function to compute rectangle perimeter
    :param side1: Length of 1 side
    :param side2: Length of 1 side
    :return: Perimeter of rectangle
    """
    return (side1 * 2) + (side2 * 2)


def square(side: float) -> float:
    """
    Function to compute square perimeter
    :param side: Length of side
    :return: Perimeter of square
    """
    return side * 4


def triangle(side1: float, side2: float, side3: float) -> float:
    """
    Function to compute triangle perimeter
    :param side1: Length of side 1
    :param side2: Length of side 2
    :param side3: Length of side 3
    :return: Perimeter of triangle
    """
    return side1 + side2 + side3
