#!/usr/bin/env python3
"""This module contains function measure_time"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    This function measures the total execution time of for wait_n
    then returns total_time / n
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    elapsed_time = time.time() - start_time
    return float(elapsed_time / n)
