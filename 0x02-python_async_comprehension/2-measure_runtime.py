#!/usr/bin/env python3
'''2-measure_runtime.py'''
import asyncio
import time
from importlib import import_module as using


async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''The function executes async_comprehension 4 times in parallel using asynci   o.gather.
    '''
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
