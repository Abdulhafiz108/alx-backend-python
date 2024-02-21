#!/usr/bin/env python3
"""This module contains function safely_get_value"""
from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default:
                     Union[T, None] = None) -> Union[Any, T]:
    """This function returns the value of a key or a default value"""
    if key in dct:
        return dct[key]
    else:
        return default
