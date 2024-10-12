"""
This module provides CLI functions for the game.
"""


def greet_user():
    """
     Main function to run CLI.
     """
    print("Добро Пожаловать в игру Мозговой Штурм!")
    name = input("Как тебя зовут? ")
    print(f"Hello, {name}!")
    return name
