#!/usr/bin/env python3

# This module should contain the paint function used in Tutorial, Task 6

def paint_can_coverage(can_size):
    """
    (str) -> float
    
    Returns the coverage in sq. meters for a given paint can size.

    Example:
    ------------
    paint_can_coverage("medium") -> 21.2
    (str) -> float
    """
    if can_size == "small":
        return 5.5
    elif can_size == "medium":
        return 21.2
    elif can_size == "large":
        return 40.5
    else:
        raise ValueError("Invalid can size. Choose 'small', 'medium', or 'large'.")