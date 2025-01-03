#!/usr/bin/env python3
""" Complex types - string and int/float to tuple"""
from typing import Callable, Iterator, Union, Optional, List, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    function takes a string k and an int or float v as arguments,
    returns a tuple.
    """

    return (k, v**2)
