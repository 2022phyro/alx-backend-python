#!/usr/bin/env python3
"""executing coroutines with async"""
import asyncio
from typing import List, Awaitable, Callable, Any

wait_random: Callable[[int], float] = __import__(
                                                 '0-basic_async_syntax'
).wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Run the wait_random function with the
    specified max_delay"""
    result: List[float] = []
    task = [asyncio.create_task(wait_random(max_delay)) for va in range(n)]

    return [await t for t in asyncio.as_completed(task)]
