#!/usr/bin/env python3
"""Introduction into async functions"""
from random import uniform
import asyncio


async def wait_random(max_delay=10):
    """An asynchronous coroutine that takes in an integer argument
    (max_delay, with a default value of 10) named wait_random
    that waits for a random delay between 0 and max_delay
    (included and float value) seconds and eventually returns it."""
    val = uniform(0, max_delay)
    await asyncio.sleep(val)
    return val
