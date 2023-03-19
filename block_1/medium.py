"""
Блок Medium:
    1. Написать функцию, которая на вход будет принимать произвольное количество аргументов и возвращать их сумму.

    2. В сигнатуре функции объявить 4 обязательных аргумента, но оставить возможность передавать в неё сколько угодно
       дополнительных аргументов. Попробуйте вызвать функцию в следующих ситуациях и объясните результат:
        - прокинуть в функцию только 1 аргумент
        - прокинуть аргументы таким образом, чтобы обязательный аргумент был передан одновременно позиционно и по ключу
        - создать кортеж со значениями и распаковать его при вызове функции с помощью *
        - создать словарь со значениями и распаковать его при вызове функции с помощью * и **: что наблюдаете? Почему?
"""


# 1. Написать функцию, которая на вход будет принимать произвольное количество аргументов и возвращать их сумму.
def sum_args(*args):
    return sum(args)


# 2. В сигнатуре функции объявить 4 обязательных аргумента, но оставить возможность передавать в неё сколько угодно
#    дополнительных аргументов.
def sum_args_with_required_args(num_1, num_2, num_3, num_4, *args):
    numbers = (num_1, num_2, num_3, num_4, *args)
    return sum(numbers)


if __name__ == '__main__':
    """ Попробуйте вызвать функцию в следующих ситуациях и объясните результат:
        - Прокинуть в функцию только 1 аргумент"""
    sum_args_with_required_args(1)
    """ Результат:
        TypeError: sum_args_with_required_args() missing 3 required positional arguments: 'num_2', 'num_3', and 'num_4'
    Так как в функции у аргументов не заданны значения по умолчанию, она не может запуститься пока не будут
    переданны все обязательные аргументы """

    "   - Прокинуть аргументы таким образом, чтобы обязательный аргумент был передан одновременно позиционно и по ключу"
    sum_args_with_required_args(1, num_1=2)
    """ Результат:
        TypeError: sum_args_with_required_args() got multiple values for argument 'num_1'
    Ошибка говорит о том, что нельзя передавать несколько раз один и тот же параметр при вызове функции """

    "- Создать кортеж со значениями и распаковать его при вызове функции с помощью *"
    args = (1, 2, 3, 4, 5)
    print(sum_args_with_required_args(*args))
