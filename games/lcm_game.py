"""
LCM Game module: The player is asked to find the least common multiple (LCM) of random numbers.
"""

import random
import math
from src.engine import play_game


def find_lcm(numbers):
    """
    Find the least common multiple (LCM) of a list of numbers.

    Args:
        numbers (list): A list of integers.

    Returns:
        int: The LCM of the numbers.
    """
    lcm = numbers[0]
    for num in numbers[1:]:
        lcm = lcm * num // math.gcd(lcm, num)
    return lcm


def lcm_game():
    """
    LCM game logic wrapped in the general game loop.
    """
    play_game(lambda: (f"{random.randint(1, 20)} {random.randint(1, 20)}",
                       find_lcm([random.randint(1, 20) for _ in range(3)])))
