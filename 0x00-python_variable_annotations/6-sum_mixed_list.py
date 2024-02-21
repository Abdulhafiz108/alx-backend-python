#!/usr/bin/env python3
"""This file contains function sum_mixed_list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """This function returns sum of a list of int and float as an float"""
    return float(sum(mxd_lst))
