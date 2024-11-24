import json

from class_books import Book

def read_file() -> list:
    """
    Прочтение файла json
    """

    with open("db_book.json", "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.decoder.JSONDecodeError:
            return []

def write_file(book:Book) -> None:
    """
    Запись в json файл
    """
    books = read_file()
    book = {
        "id": book.id,
        "title": book.title,
        "author": book.author,
        "year": book.year,
        "status": book.status
    }
    books.append(book)
    with open("db_book.json", "w", encoding="utf-8") as file:
        json.dump(books, file, ensure_ascii=False, indent=5)

