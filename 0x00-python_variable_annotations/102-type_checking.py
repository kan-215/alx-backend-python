#!/usr/bin/env python3
""" 
Type Checking Example Script 
This script defines a function to zoom in on the elements of a tuple by repeating each element
a specified number of times. It demonstrates type checking with Python's typing module.
"""

from typing import Tuple, List

def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """
    Function to zoom in on a tuple by repeating each element in the tuple 'factor' times.
    
    Args:
    lst (Tuple[int, ...]): A tuple of integers to be zoomed in.
    factor (int): The number of times each element in the tuple is repeated. Defaults to 2.
    
    Returns:
    List[int]: A list of integers where each element in the input tuple is repeated 'factor' times.
    """
    # List comprehension to repeat each item in the tuple 'factor' times
    zoomed_in: List[int] = [
        item for item in lst  # For each item in the tuple
        for i in range(factor)  # Repeat the item 'factor' times
    ]
    return zoomed_in  # Return the new list with repeated elements

# Sample tuple of integers
array = (12, 72, 91)

# Call zoom_array with the default factor of 2 (each element will be repeated twice)
zoom_2x = zoom_array(array)

# Call zoom_array with a factor of 3 (each element will be repeated three times)
zoom_3x = zoom_array(array, 3)

# Print the results to verify the function's output
print("Zoom 2x:", zoom_2x)
print("Zoom 3x:", zoom_3x)

