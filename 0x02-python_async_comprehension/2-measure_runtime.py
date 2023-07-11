#!/usr/bin/env python3
"""Using asyncio.gather to run co-routines
in parallel"""

from asyncio import gather
from time import perf_counter

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    routines = [async_comprehension() for _ in range(4)]
    tpc = perf_counter()
    await gather(*routines)
    timeup = perf_counter() - tpc
    return timeup
