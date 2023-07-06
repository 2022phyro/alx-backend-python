#!/usr/bin/env python3
"""Duck typing yay"""
from typing import Iterable, Tuple, Sequence, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Duck typing an iterable"""
    return [(i, len(i)) for i in lst]
