#!/usr/bin/env python3
"""Asynchronous comprehensions: In this we are introduced into that stuff"""

import asyncio
from typing import AsyncGenerator
from random import uniform


async def async_generator() -> AsyncGenerator[float, None]:
    """This async generator yields 10 random numbers
    between one and 10"""
    for i in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
