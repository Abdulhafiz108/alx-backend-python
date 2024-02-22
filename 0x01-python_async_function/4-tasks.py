#!/usr/bin/env python3
"""This module contains function wait_n"""
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    This function spawns task_wait_random n times with the specified max_delay
    then returns a list of the delays in ascending order
    """
    delays = []

    async def wait_and_add_delay(delay):
        """
        Helper function to wait for a random delay and add to the delays list
        """
        random_delay = await task_wait_random(max_delay)
        delays.append(random_delay)

    tasks = [wait_and_add_delay(delay) for delay in range(n)]
    await asyncio.gather(*tasks)

    return delays
