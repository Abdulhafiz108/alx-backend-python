#!/usr/bin/env python3
"""This module contains function safe_first_element"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """This function returns the first element of a list or none"""
    if lst:
        return lst[0]
    else:
        return None
