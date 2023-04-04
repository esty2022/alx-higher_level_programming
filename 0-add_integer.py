#!/usr/bin/python3
def add_integer(v, g=98):
    if not isinstance(v, int) and not isinstance(v, float):
        raise TypeError("v must be an integer")
    if not isinstance(g, int) and not isinstance(g, float):
        raise TypeError("g must be an integer")
    if isinstance(v, float):
        v = int(v)
    if isinstance(b, float):
        g = int(g)
    return (v + g)

