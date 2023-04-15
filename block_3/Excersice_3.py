"""
Задача 3

3.1 Написать кэширующий декоратор. Суть в том, что если декорируемая функция будет запущена с теми параметрами
    с которыми она уже запускалась - брать результат из кэша и не производить повторное выполнение функции.

3.2 Сделать так, чтобы информация в кэше была актуальной не более 10 секунд.
    Предусмотреть механизм автоматической очистки кэша в процессе выполнения функций.

3.3 Параметризовать время кэширования в декораторе.
"""
from time import sleep
from typing import Callable, Any
from expiringdict import ExpiringDict


# 3.1 Написать кэширующий декоратор. Суть в том, что если декорируемая функция будет запущена с теми параметрами
#     с которыми она уже запускалась - брать результат из кэша и не производить повторное выполнение функции.
#
# 3.2 Сделать так, чтобы информация в кэше была актуальной не более 10 секунд.
#     Предусмотреть механизм автоматической очистки кэша в процессе выполнения функций.
def chache_ten_seconds_deco(func) -> Callable:
    cache = ExpiringDict(max_len=100, max_age_seconds=10, items={})  # Объект кеша
    func_name = func.__name__  # Имя функции для которой сохраняется кеш

    def wrapper(*args, **kwargs) -> Any:
        params: str = prepare_params_view(args=args, kwargs=kwargs)
        # Проверим есть ли готовый результат в кеше
        existing_result: Any = cache.get(func_name, {}).get(params)
        if existing_result is not None:
            # Если есть - вернем результат
            print('Сработал Кеш')
            return existing_result
        else:
            # Если нет - сохраним в кеш и запустим функцию
            result = func(*args, **kwargs)
            if func_name not in cache:
                cache[func_name] = {params: None}
            cache[func_name][params] = result
            print('Данных в кеше нет. Выполнилась функция')
            return result

    def prepare_params_view(args: tuple, kwargs: dict) -> str:
        """
        Подготавливает строковое представление заданных параметров
        """
        # Необходимо отсортировать словарь, что бы иметь одинаковый порядок
        kwargs_params = list(kwargs.items())
        kwargs_params.sort(key=lambda x: x[0])  # Сортировка по ключу
        return f"{args} {kwargs}"

    return wrapper


@chache_ten_seconds_deco
def sum_func(a, b):
    return a + b


if __name__ == '__main__':
    # Продемонстрируем работу с одним и тем же значением
    for i in range(12):
        print(f"Запуск на {i + 1} секунде: ", end='')
        sum_func(1, 2)
        sleep(1)


# 3.3 Параметризовать время кэширования в декораторе.
def cache_n_seconds(n_seconds: int = 10) -> Callable:

    def chache_deco(func) -> Callable:
        cache = ExpiringDict(max_len=100, max_age_seconds=n_seconds, items={})  # Объект кеша
        func_name = func.__name__  # Имя функции для которой сохраняется кеш

        def wrapper(*args, **kwargs) -> Any:
            params: str = prepare_params_view(args=args, kwargs=kwargs)
            # Проверим есть ли готовый результат в кеше
            existing_result: Any = cache.get(func_name, {}).get(params)
            if existing_result is not None:
                # Если есть - вернем результат
                print('Сработал Кеш')
                return existing_result
            else:
                # Если нет - сохраним в кеш и запустим функцию
                result = func(*args, **kwargs)
                if func_name not in cache:
                    cache[func_name] = {params: None}
                cache[func_name][params] = result
                print('Данных в кеше нет. Выполнилась функция')
                return result

        def prepare_params_view(args: tuple, kwargs: dict) -> str:
            """
            Подготавливает строковое представление заданных параметров
            """
            # Необходимо отсортировать словарь, что бы иметь одинаковый порядок
            kwargs_params = list(kwargs.items())
            kwargs_params.sort(key=lambda x: x[0])  # Сортировка по ключу
            return f"{args} {kwargs}"

        return wrapper

    return chache_deco


@cache_n_seconds(n_seconds=3)
def sum_func(a, b):
    return a + b


if __name__ == '__main__':
    # Продемонстрируем работу с одним и тем же значением
    for i in range(12):
        print(f"Запуск на {i + 1} секунде: ", end='')
        sum_func(1, 2)
        sleep(1)
