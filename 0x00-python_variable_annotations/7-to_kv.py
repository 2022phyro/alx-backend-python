#!/usr/bin/env python3
"""Annotations for optional"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple with above annotations"""
    return (k, v ** 2)
