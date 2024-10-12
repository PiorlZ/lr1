"""
Progression Game module: The player is asked to find the missing number in a geometric progression.
"""

import sys
import os
import random
from src.engine import play_game
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def generate_progression():
    """
    Generate a geometric progression with a missing number.

    Returns:
        tuple: A progression with one number replaced by '..' and the correct answer.
    """
    start = random.randint(1, 10)
    multiplier = random.randint(2, 5)
    length = 10
    progression = [start * (multiplier ** i) for i in range(length)]
    missing_index = random.randint(0, length - 1)
    correct_answer = progression[missing_index]
    progression[missing_index] = '..'
    return ' '.join(map(str, progression)), correct_answer

def progression_game():
    """
    Geometric progression game logic wrapped in the general game loop.
    """
    play_game(generate_progression)
