#!/usr/bin/env python3
"""Takes a float and returns a function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a callable that multiplies a number"""
    def mul(x: float) -> float:
        """The callable"""
        return x * multiplier
    return mul
