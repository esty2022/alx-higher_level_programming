#!/usr/bin/python3
"""explain a JSON-to-object function."""
import json


def from_json_string(my_str):
    """reload the Return the Python object representation of a JSON string."""
    return json.loads(my_str)
