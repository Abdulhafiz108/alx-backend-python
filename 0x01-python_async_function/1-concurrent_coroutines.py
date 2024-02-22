#!/usr/bin/env python3
"""This module contains function wait_n"""
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    This function spawns wait_random n times with the specified max_delay
    then returns a list of the delays in ascending order
    """
    delays = []
    times = n
    while times > 0:
        delays.append(await wait_random(max_delay))
        times = times - 1

    return sorted(delays)
