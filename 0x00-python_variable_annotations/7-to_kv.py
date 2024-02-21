#!/usr/bin/env python3
"""This module contains a function to_kv"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """This function takes a string and an int or float then returns a tuple"""
    return (k, v * v)
