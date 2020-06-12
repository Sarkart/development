import numpy as np


def game_core_v1(number):
    '''Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    while True:
        count += 1
        predict = np.random.randint(1, 101)  # предполагаемое число
        if number == predict:
            return (count)  # выход из цикла, если угадали


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return (score)


def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    predict = np.random.randint(1, 101)
    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1
    return (count)  # выход из цикла, если угадали


def game_core_v3(number):
    """Берём среднее между минимальным и максимальным значениями, далее проверяем наше число с загаданным.
    В зависимости от того, меньше или больше нужного наше число,
    функция сокращает область поиска в два раза в нужную сторону"""
    count = 1
    bottom = 1
    top = 100
    predict = (bottom+top) // 2
    while number != predict:
        count += 1
        predict = (bottom+top) // 2     # необходимо повторить операцию, иначе область поиска будет сужаться медленнее
        if number > predict:
            bottom = predict + 1        # если загаданное число меньше, поднимаем нижнюю границу поиска
            predict += 1
        else:
            top = predict - 1
            predict -= 1
    return count  # выход из цикла, если угадали


score_game(game_core_v3)
