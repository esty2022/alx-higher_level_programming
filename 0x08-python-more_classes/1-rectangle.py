#!/usr/bin/python3
# 1-rectangle.py
"""Defines a Rectangle class."""

class Rectangle:
    """Represent a rectangle."""

    def __init__(user, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        user.width = width
        self.height = height

    @property
    def width(user):
        """Get/set the width of the rectangle."""
        return user.__width

    @width.setter
    def width(user, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        user.__width = value

    @property
    def height(user):
        """Get/set the height of the rectangle."""
        return user.__height

    @height.setter
    def height(user, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        user.__height = value

