"""
Задача 1

1.1 Написать декоратор, который перед запуском произвольной функции с произвольным набором аргументов будет показывать
    в консоли сообщение "Покупайте наших котиков!" и возвращать результат запущенной функции.

1.2 Параметризовать декоратор таким образом, чтобы сообщение, печатаемое перед выполнением функции можно было задавать
    как параметр во время декорирования.
"""
from typing import Callable, Any


# 1.1 Написать декоратор, который перед запуском произвольной функции с произвольным набором аргументов будет показывать
#     в консоли сообщение "Покупайте наших котиков!" и возвращать результат запущенной функции.
def particular_message_deco(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> Any:
        print("Покупайте наших котиков!")
        return func(*args, **kwargs)

    return wrapper


@particular_message_deco
def some_func():
    """Функция для декорирования"""
    print("--- Запуск основной функции ---")


if __name__ == '__main__':
    some_func()


# 1.2 Параметризовать декоратор таким образом, чтобы сообщение, печатаемое перед выполнением функции можно было задавать
#     как параметр во время декорирования.
def print_message_before_run_func(message: str) -> Callable:
    def message_deco(func: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> Any:
            print(message)
            return func(*args, **kwargs)

        return wrapper

    return message_deco


@print_message_before_run_func(message='Собственное сообщение перед запуском функции')
def some_func():
    """Функция для декорирования"""
    print("--- Запуск основной функции ---")


if __name__ == '__main__':
    some_func()
