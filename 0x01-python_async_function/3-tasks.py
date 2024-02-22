#!/usr/bin/env python3
"""this module contains the function task_wait_random"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """This function returns an asyncio.Task"""
    return asyncio.create_task(wait_random(max_delay))
