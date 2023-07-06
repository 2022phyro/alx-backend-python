#!/usr/bin/env python3
"""Annotations for unknown lists"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Checks if the element is a sequence"""
    if lst:
        return lst[0]
    else:
        return None
