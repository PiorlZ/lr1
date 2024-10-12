"""
Common functions used across different games.
"""


def check_answer(user_answer, correct_answer):
    """
    Check if the user's answer is correct.

    Args:
        user_answer (int): The answer given by the user.
        correct_answer (int): The correct answer.

    Returns:
        bool: True if the answer is correct, False otherwise.
    """
    if user_answer == correct_answer:
        print("Правильно!")
        return True

    print(f"'{user_answer}' это неверный ответ ;(. "
          f"Правильным ответом было '{correct_answer}'.")
    print("Попробуй еще!")
    return False


def play_game(get_question_and_answer):
    """
    General game loop for playing a game.

    Args:
        get_question_and_answer (function): Function that returns a question and the correct answer.
    """
    for _ in range(3):
        question, correct_answer = get_question_and_answer()
        print(f"Вопрос: {question}")
        user_answer = int(input("Твой ответ: "))

        if check_answer(user_answer, correct_answer):
            continue
        return

    print("Поздравляю!")
