import json

from class_books import Book
from file_saver import write_file, read_file
from services import out_red_text, out_green_text


def adding_book():
    """
    Добавление книги
    """

    title = input("Введите название книги: ")
    author = input("Введите автора книги: ")
    while True:
        year = input("Введите год выпуска книги: ")
        if year.isdigit():
            book = Book(title, author, int(year))
            write_file(book)
            print(out_green_text("Книга добавлена!"))
            break
        else:
            print(out_red_text("Введен некорректный год!"))

def delete_book():
    while True:
        books = read_file()

        if not books:
            print("Пока нет добавленных книг!\n")
            break

        book_id = input("Введите id книги которую хотите удалить: ")

        if book_id.isdigit():
            for book in books:
                if int(book["id"]) == int(book_id):
                    books.remove(book)
                    with open("db_book.json", "w", encoding="utf-8") as file:
                        json.dump(books, file, ensure_ascii=False)
                    print(out_green_text(f"Книга с id:{book_id} удален."))
                    break
            else:
                print("Книги с таким id не найдено!")
            break
        else:
            print(out_red_text("Введен некорректный id!"))

def search_book():
    """
    Поиск книги по автору, названию книги, году
    """
    search_user = input("Поиск: ").strip()
    books = read_file()
    indicator = 1
    for book in books:
        if search_user in book["author"] or search_user in book["title"] or search_user in str(book["year"]):
            print(Book(**book))
            indicator = 0
    if indicator:
        print("Книга не найдена!")

def views_books():
    """
    Вывод списка всех книг
    """
    books = read_file()
    for num, value in enumerate(books, 1):
        print(num, Book(**value))








if __name__ == "__main__":
    views_books()