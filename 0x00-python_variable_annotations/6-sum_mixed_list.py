#!/usr/bin/env python3
"""Annotations for lists"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sums up a mixed list"""
    return sum(mxd_lst)
