"""
Задача 5

После решения задач написать функцию и задекорировать её сразу несколькими из созданных декораторов, посмотреть
на результат и суметь объяснить его.

Потом поменять порядок декорирования и проделать то же самое.
"""
from typing import Callable, Any


def first_decorator(func: Callable) -> Callable:
    print('Декорирование first_decorator')

    def wrapper(*args, **kwargs) -> Any:
        print('first_decorator')
        return func(*args, **kwargs)

    return wrapper


def second_decorator(func: Callable) -> Callable:
    print('Декорирование second_decorator')

    def wrapper(*args, **kwargs) -> Any:
        print('second_decorator')
        return func(*args, **kwargs)

    return wrapper


@second_decorator
@first_decorator
def some_func():
    """Декорируемая функция"""
    print('---Код основной функции---')


if __name__ == "__main__":
    print()
    some_func()
    """
    Вывод в консоль:
        Декорирование first_decorator
        Декорирование second_decorator
        
        second_decorator
        first_decorator
        ---Код основной функции---
        
    Здесь видим что декоратор который ближе к функции в синтаксическом сахаре 
    декорирует первым но выполняется последним
    """


# Поменяем порядок
@first_decorator
@second_decorator
def some_func():
    """Декорируемая функция"""
    print('---Код основной функции---')


if __name__ == "__main__":
    print()
    some_func()
    """
        Вывод в консоль:
            Декорирование second_decorator
            Декорирование first_decorator
            
            first_decorator
            second_decorator
            ---Код основной функции---

        Здесь обратная ситуация
        """
