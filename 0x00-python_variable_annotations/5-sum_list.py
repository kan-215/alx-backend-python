#!/usr/bin/env python3
"""Complex types - list of floats"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
        A type-annotated function sum_list that takes a
        list input_list of floats as argument and returns
        their sum as a float.
    """
    return sum(input_list)
