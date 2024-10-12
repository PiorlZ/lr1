import sys
import os
from src.cli import greet_user
from games import lcm_game, progression_game
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def main():
    greet_user()
    print("Выберите игру:")
    print("1. Игра НОК (Наименьшее общее кратное)")
    print("2. Игра Геометрическая прогрессия")

    choice = input("Ваш выбор (1 или 2): ")

    if choice == '1':
        lcm_game.lcm_game()
    elif choice == '2':
        progression_game.progression_game()
    else:
        print("Некорректный выбор!")


if __name__ == "__main__":
    main()
