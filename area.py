import math
"""
A module to compute area of shapes
"""


def cir(num: float) -> float:
    """
    Function to compute area of a circle
    :param num: Length of radius
    :return: Area of a circle
    """
    return num * num * math.pi


def rec(num1: float, num2: float) -> float:
    """
    Function to compute area of a rectangle
    :param num1: Length of side 1
    :param num2: Length of side 2
    :return: Area of a rectangle
    """
    return num1 * num2


def squ(num: float) -> float:
    """
    Function to compute area of a square
    :param num:  Length of a side
    :return: Area of a square
    """
    return num * num


def tri(num1: float, num2: float) -> float:
    """
    Function to compute area of a triangle
    :param num1: Length of side 1
    :param num2: Length of side 2
    :return: Area of a triangle
    """
    return (num1 * num2)/2
