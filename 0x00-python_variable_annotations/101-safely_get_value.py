#!/usr/bin/env python3
"""Using TypeVar and typing for dicts"""
from typing import Union, Any, Mapping, TypeVar


T = TypeVar('T')


def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Union[T, None] = None
) -> Union[Any, T]:
    """Safely get the value of a dict"""
    if key in dct:
        return dct[key]
    else:
        return default
