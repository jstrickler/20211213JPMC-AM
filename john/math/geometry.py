"""
Geometric routines

circle_area()  -- takes diameter
rectangle_area() -- takes length and width
"""
import math

spam = 25

def circle_area(diameter):
    """
    Compute area of a circle

    :param diameter: Diameter of circle
    :return: Area of circle
    """
    radius = diameter / 2
    return math.pi * (radius ** 2)

def rectangle_area(length, width):
    """
    Compute area of a rectangle, given length and width

    :param length: Length of rectangle
    :param width: Width of rectangle
    :return: Area of rectangle
    """
    return length * width

# "private"
def _not_public():
    pass
