#!/usr/bin/env python3
"""This module contains asynchronous function wait_random"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    This function waits a random float value between 0 and max_delay
    Then returns the random float
    """
    random_float = random.uniform(0, max_delay)
    await asyncio.sleep(random_float)
    return random_float
