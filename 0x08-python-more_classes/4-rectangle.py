#!/usr/bin/python3
# 4-rectangle.py
# ALX SE SCHOOL
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(breadth, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        breadth.width = width
        breadth.height = height

    @property
    def width(breadth):
        """Get/set the width of the Rectangle."""
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
        """Get/set the height of the Rectangle."""
        return breadth.__height

    @height.setter
    def height(breadth, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        breadth.__height = value

    def area(breadth):
        """Return the area of the Rectangle."""
        return (breadth.__width * breadth.__height)

    def perimeter(breadth):
        """Return the perimeter of the Rectangle."""
        if breadth.__width == 0 or breadth.__height == 0:
            return (0)
        return ((breadth.__width * 2) + (breadth.__height * 2))

    def __str__(breadth):
        """Return the printable representation of the Rectangle.
        Represents the rectangle with the # character.
        """
        if breadth.__width == 0 or breadth.__height == 0:
            return ("")

        rect = []
        for i in range(breadth.__height):
            [rect.append('#') for j in range(breadth.__width)]
            if i != breadth.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(breadth):
        """Return the string representation of the Rectangle."""
        rect = "Rectangle(" + str(breadth.__width)
        rect += ", " + str(breadth.__height) + ")"
        return (rect)

