#!/usr/bin/env python3
"""This module contains function async_comprehension"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """This function collects and return 10 random float"""
    return [value async for value in async_generator()]
