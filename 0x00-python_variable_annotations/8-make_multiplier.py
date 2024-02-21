#!/usr/bin/env python3
"""This module contains function make_multiplier"""
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """This function takes a float and eturns a function that 
    multiplies a float by multiplier"""
    
    def made_multiplier(n: float) -> float:
        return n * multiplier
    
    return made_multiplier
