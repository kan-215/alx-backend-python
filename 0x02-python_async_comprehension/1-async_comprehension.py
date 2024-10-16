#!/usr/bin/env python3
'''1-async_comprehension.py
'''
from typing import List
from importlib import import_module as using


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''The function creates a list of 10 numbers from a 10-number generator.
    '''
    return [num async for num in async_generator()]
