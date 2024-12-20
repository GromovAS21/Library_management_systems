import json


def read_file() -> list:
    """
    Прочтение файла json
    """

    with open("db_book.json", "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.decoder.JSONDecodeError:
            return []


def write_file(books: list) -> None:
    """
    Запись в json файл
    """

    with open("db_book.json", "w", encoding="utf-8") as file:
        json.dump(books, file, ensure_ascii=False, indent=5)
