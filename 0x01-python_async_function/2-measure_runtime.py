#!/usr/bin/env python3
"""Measuring the runtime of our await functions"""
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n, max_delay):
    """Measures the time it takes wait_n to run"""
    start_time = time.time()
    await wait_n(n, max_delay)
    end_time = time.time()
    return float(end_time - start_time)
