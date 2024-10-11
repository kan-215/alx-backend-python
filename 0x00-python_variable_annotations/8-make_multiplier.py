#!/usr/bin/env python3
"""Basic annotations - make_multiplier"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """make_multiplier function"""

    return lambda x: x * multiplier
