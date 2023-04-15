"""
Задача 6

6.1 Написать декоратор, который будет запрашивать у пользователя пароль при попытке функции осуществить вызов.
    Если введён верный пароль, то функция будет выполнена и вернется результат её работы.
    Если нет - в консоли появляется соответствующее сообщение.

6.2 Параметризовать декоратор таким образом, чтобы можно было задавать
    индивидуальный пароль для каждой декорируемой функции.
"""
from typing import Callable, Any


def func_password_deco(valid_password: str):
    def func_password(func: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> Any:
            password = input(f'Введите пароль для запуска "{func.__name__}": ')
            if password == valid_password:
                return func(*args, **kwargs)
            print('(!) Неверный пароль для запуска функции')

        return wrapper

    return func_password


@func_password_deco(valid_password='1234')
def some_func():
    """Декорируемая функция"""
    print('---Код основной функции---')


if __name__ == '__main__':
    some_func()
