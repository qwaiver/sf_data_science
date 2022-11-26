import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0 # количество попыток
    predict_number = np.random.randint(0, 101)  # предполагаемое число
    while True:
        count += 1
        if number == predict_number:
            break
        elif number < predict_number:
            number += 8
        elif number > predict_number:
            number -= 3
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array: #запускаем цикл for 1000 раз
        count_ls.append(random_predict(number)) #добавляем кол-во попыток в список

    score = int(np.mean(count_ls)) # находим среднее количество попыток
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
