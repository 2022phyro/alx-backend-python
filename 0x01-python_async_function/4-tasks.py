#!/usr/bin/env python3
"""Running a task"""
import asyncio
from typing import List, Awaitable, Callable, Any

task_wait_random: Callable[[int], float] = __import__(
                                                  '3-tasks'
).wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Run the wait_random function with the
    specified max_delay"""
    task = [task_wait_random(max_delay) for va in range(n)]

    return [await t for t in asyncio.as_completed(task)]
