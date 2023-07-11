#!/usr/bin/env python3
"""Using asyncio.gather to run co-routines
in parallel"""

from asyncio import gather
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():

