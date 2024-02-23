#!/usr/bin/env python3
"""This module contains function measure_runtime"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    This function executes async_comprehension four times in parallel
    and returns its execution timne
    """
    start_time = time.time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    return time.time() - start_time
