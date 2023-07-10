#!/usr/bin/python3
"""executing coroutines with async"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """Run the wait_random function with the
    specified max_delay"""
    result = []
    for i in range(n):
        x = await wait_random(max_delay)
        result.append(x)

    return result
