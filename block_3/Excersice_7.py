"""
Задача 7

7.1 Написать декоратор, который после выполнения функции будет возвращать результат и записывать его в текстовый файл.

7.2 Модернизировать декоратор таким образом, чтобы можно было не только осуществлять запись в файл,
    но и в целом производить любую операцию логирования или оповещения.

7.3 Доработать декоратор таким образом, чтобы можно было при декорировании можно было передавать список нотификаторов.
"""
from typing import Callable, Any, List


# 7.1 Написать декоратор, который после выполнения функции будет возвращать результат и записывать его в текстовый файл.
def log_to_file_deco(filename: str):
    def log_to_file(func: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> Any:
            result = func(*args, **kwargs)
            with open(filename, "w", encoding="UTF-8") as file:
                file.write(str(result))
            return result

        return wrapper

    return log_to_file


@log_to_file_deco(filename='test.txt')
def some_func():
    """Декорируемая функция"""
    return "Результат работы функции"


if __name__ == "__main__":
    print(some_func())


# 7.2 Модернизировать декоратор таким образом, чтобы можно было не только осуществлять запись в файл,
#     но и в целом производить любую операцию логирования или оповещения.
def log_to_file(result: Any):
    with open("log.txt", "w", encoding="UTF-8") as file:
        file.write(str(result))


def log_to_file_deco_2(log_func: Callable):
    def log_to_file(func: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> Any:
            result = func(*args, **kwargs)
            log_func(result)
            return result

        return wrapper

    return log_to_file


@log_to_file_deco_2(log_func=log_to_file)
def some_func():
    """Декорируемая функция"""
    return "Результат работы функции"


if __name__ == "__main__":
    print(some_func())


# 7.3 Доработать декоратор таким образом, чтобы можно было при декорировании можно было передавать список нотификаторов.
class FakeDB:
    """Класс для имитации работы с БД"""

    def execute(self, query):
        print('Пишем в БД')
        return 1


class FakeRequests:
    """Класс для имитации работы модуля requests"""
    response_string = ('{"ok":true,"result":{"message_id": 1,"from":'
                       '{"id":1,"is_bot":true,"first_name":"Nikolay","username":"nikolay"}}}')

    def get(self, *args, **kwargs):
        return self

    @property
    def text(self):
        return FakeRequests.response_string

    def json(self):
        import json
        return json.loads(self.text)

    def __repr__(self):
        return "<Response [200]>"


def notifier_1(result):
    db = FakeDB()
    query = ('INSERT INTO logs.func_log ("result") '
             f'VALUES ({result});')
    db.execute(query)


def tg_notifier(result, token='A32S!FSADfdsf43'):
    url_telegram = f"https://api.telegram.org/bot{token}/"
    requests = FakeRequests()
    requests.get(url_telegram + 'sendMessage',
                 params={'text': str(result),
                         'chat_id': 1})


def log_to_file_with_notifiers_deco(log_funcs: List[Callable]):
    def log_to_file(func: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> Any:
            result = func(*args, **kwargs)
            [log_func(result) for log_func in log_funcs]
            return result

        return wrapper

    return log_to_file


@log_to_file_with_notifiers_deco(log_funcs=[notifier_1, tg_notifier])
def some_func():
    """Декорируемая функция"""
    return "Результат работы функции"


if __name__ == "__main__":
    print(some_func())
