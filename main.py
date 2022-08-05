"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    predict_number=50 #начальное приближение
    l_bound=1 #нижняя возможная граница угадываемого числа
    u_bound=100 #верхняя возможная граница угадываемого числа
    while True:
        count += 1
        if number == predict_number:
            break  # выход из цикла если угадали
        else:
            # если угадываемое число вышло за возможные границы (из-за округления), то возвращаем число в границы
            if predict_number<l_bound or predict_number>u_bound:
                predict_number=l_bound
                continue
            # если число не угадано, то определяем новые возможные границы угадываемого числа и задаем
            # угадываемое число как середину диапазона
            if number>predict_number:
                l_bound=predict_number+1
                predict_number=int((u_bound+predict_number)/2)
            if number<predict_number:
                u_bound=predict_number-1
                predict_number=int((l_bound+predict_number)/2)
            
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)