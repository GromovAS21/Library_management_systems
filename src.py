from class_books import Book
from file_saver import write_file


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
            print("Книга добавлена!")
            break



if __name__ == "__main__":
    adding_book()