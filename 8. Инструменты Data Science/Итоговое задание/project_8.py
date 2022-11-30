import numpy as np


def random_predict(number: int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0 # Количество попыток
    predict_number = 35  # Предполагаемое число
    while True:
        count += 1
        if number == predict_number:
            break
        elif number > predict_number:
            predict_number += 7
        elif number < predict_number:
            predict_number -= 3
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает 
    наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = [] # Список для сохранения количества попыток
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000)) 
    # Загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number)) 

    score = int(np.mean(count_ls)) # Находим среднее количество попыток
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
