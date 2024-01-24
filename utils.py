import json


def get_all_operations(path) -> list[dict]:
    """
    Функция получения операций из файла
    :param path: путь к файлу
    :return: json с операциями
    """
    with open(path, encoding='utf-8') as file:
        return json.load(file)


