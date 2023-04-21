"""
1. Написать ещё несколько произвольных функций (3-4 штуки) и решить задачу со счетчиком аналогично той,
   которая была решена для запуска функции суммирования.

2. Написать функцию, внутри которой у нас будет объявляться наша функция суммирования и возвращаться
   в качестве результата работы из объемлющей функции.

3. Попробуйте вызвать написанную функцию и сохраните результат её работы в переменную.
   Напечатайте результат на экран. Что наблюдаете?

4. Осуществите вызов функции суммирования из полученной переменной.
"""
from typing import Union, Callable

calls_cnt = {}  # Количество запусков функций


def count_function_calls(func_name: str) -> int:
    """
    Подсчитывает кол-во запусков функции суммирования
    """
    global calls_cnt
    if func_name not in calls_cnt:
        calls_cnt[func_name] = 0
    calls_cnt[func_name] += 1
    return calls_cnt[func_name]


# 1. Написать ещё несколько произвольных функций (3-4 штуки) и решить задачу со счетчиком аналогично той,
#    которая была решена для запуска функции суммирования.
def upper_user_name(user_name: str) -> str:
    """
    Делает имя пользователя заглавными буквами
    """
    count_function_calls(func_name='upper_user_name')
    return user_name.upper()


def lower_user_name(user_name: str) -> str:
    """
    Делает имя пользователя строчными буквами
    """
    count_function_calls(func_name='lower_user_name')
    return user_name.lower()


def count_args(*args) -> int:
    """
    Считает кол-во переданных аргументов
    """
    count_function_calls(func_name='count_args')
    return len(args)


if __name__ == '__main__':
    for i in range(10):
        upper_user_name('John')
        if i % 2 != 0:  # Чтобы не было совпадений по кол-ву запусков
            lower_user_name('John')
        count_args(1, 2, 3, 4)

    for f_name, calls in calls_cnt.items():
        print(f"Произошло {calls} запуска(ов) функции {f_name}")


# 2. Написать функцию, внутри которой у нас будет объявляться наша функция суммирования и возвращаться
#    в качестве результата работы из объемлющей функции.
def return_sum_func() -> Callable:
    """Функция возвращающая функцию суммирования"""

    def sum_args(*args) -> Union[int, float]:
        """Функция суммирования"""
        return sum(args)

    return sum_args


# 3. Попробуйте вызвать написанную функцию и сохраните результат её работы в переменную.
#    Напечатайте результат на экран. Что наблюдаете?
if __name__ == '__main__':
    sum_func = return_sum_func()
    print(sum_func)
    """ 
    Результат:
        <function return_sum_func.<locals>.sum_args at 0x0000018CAA33E430>
        Здесь мы видим название функции, и что она находится в локальной области видимости функции "return_sum_func"
    """

    # 4. Осуществите вызов функции суммирования из полученной переменной.
    print(sum_func(1, 1, 1))
