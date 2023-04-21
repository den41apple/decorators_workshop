"""
Задача 4

4.1 Написать декоратор, который бы измерял время работы функции и печатал бы его на экран.

4.2 Доработать декоратор таким образом, чтобы в логах было название запускаемой функции помимо времени исполнения.

4.3 Доработать декоратор так, чтобы запись лога для функции велась в файл, путь к которому нужно было бы задавать
    во время декорирования как параметр.
"""
from datetime import datetime
from time import sleep
from typing import Callable, Any, Union, TextIO


def calculate_time_deco(file: str = None) -> Callable:


    def calculate_time(func: Callable) -> Callable:
        nonlocal file
        function_name = func.__name__

        def wrapper(*args, **kwargs) -> Any:
            nonlocal file
            start_time = datetime.now()
            result = func(*args, **kwargs)
            time_difference = datetime.now() - start_time
            message = f'Функция "{function_name}" выполнилась за {time_difference}'
            # В зависимости от того куда сохраняем
            if isinstance(file, str):
                with open(file, 'w', encoding='UTF-8') as file:
                    print(message, file=file)
            else:
                print(message)
            return result

        return wrapper

    return calculate_time


@calculate_time_deco()
def some_func():
    sleep(1)


@calculate_time_deco(file='test.txt')
def some_func_to_file():
    sleep(1)


if __name__ == '__main__':
    some_func()  # Вывод в консоль
    some_func_to_file()  # Вывод в файл
