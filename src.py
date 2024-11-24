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





if __name__ == "__main__":
    adding_book()
    delete_book()
