#!/usr/bin/env python3
"""This module contains function async_generator"""
import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[int, None, None]:
    """
    This function loops 10 times and yield a random number from 1-10
    """
    i = 0
    while i < 10:
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
        i += 1
