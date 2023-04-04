#!/usr/bin/python3
# 1-rectangle.py
# ALX SE CLASS
"""Explian Rectangle class."""


class Rectangle:
    """specify a rectangle."""

    def __init__(breadth, width=0, height=0):
        """Initialize a new Rectangle.
        Arguments:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        breadth.width = width
        breadth.height = height

    @property
    def width(breadth):
        """Get/set the width of the rectangle."""
        return breadth.__width

    @width.setter
    def width(breadth, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        breadth.__width = value

    @property
    def height(breadth):
        """Get/set the height of the rectangle."""
        return breadth.__height

    @height.setter
    def height(breadth, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        breadth.__height = value

