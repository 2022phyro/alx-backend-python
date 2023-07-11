#!/usr/bin/env python3
"""Using async comprehensions over an async generator"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List:
    """Returns the 10 random numbers from our
    async generator"""
    return [i async for i in async_generator()]
