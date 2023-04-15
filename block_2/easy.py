"""
1. Реализовать счетчик, который будет увеличиваться каждый раз, когда у нас осуществляется запуск функции суммирования.
"""
from typing import Union

calls_cnt = 0  # Количество запусков функции суммирования


def sum_args(*args) -> Union[int, float]:
    """Функция суммирования"""
    count_function_calls()
    return sum(args)


def count_function_calls() -> int:
    """
    Подсчитывает кол-во запусков функции суммирования
    """
    global calls_cnt
    calls_cnt += 1
    return calls_cnt


def get_calls_cnt() -> int:
    """Геттер для pytest"""
    return calls_cnt


def refresh_calls_cnt() -> None:
    """Обнуляет calls_cnt для pytest"""
    global calls_cnt
    calls_cnt = 0


if __name__ == '__main__':
    for i in range(10):
        sum_args(1, 2, 3, 4)
        print(f"Произошло {calls_cnt} запуска(ов) функции суммирования")
