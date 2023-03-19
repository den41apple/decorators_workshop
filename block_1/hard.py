"""
Блок Hard
    1. Модифицировать функцию таким образом, чтобы для суммирования брались только:
       - обязательные аргументы
       - первые 2 аргумента из дополнительных позиционных аргументов
       - и любой аргумент из дополнительных аргументов (если они есть), переданных по ключу (если они есть).
"""
from random import choice


def sum_args_with_required_args(num_1, num_2, num_3, num_4, *args, **kwargs):
    args = list(args)
    # - обязательные аргументы
    numbers = [num_1, num_2, num_3, num_4]
    numbers += args[:2]
    # и любой аргумент из дополнительных аргументов (если они есть), переданных по ключу (если они есть).
    additional_numbers = args[2:] + list(kwargs.values())
    numbers.append(choice(additional_numbers))
    return sum(numbers)
