from class_books import Book
from file_saver import write_file, read_file
from services import out_red_text, out_green_text

exceptions_book_id =  out_red_text("Введен некорректный ID!")
exceptions_book_found = "Книга c указанным ID не найдена!"

def adding_book():
    """
    Добавление книги в файл JSON
    """

    title = input("Введите название книги: ")
    author = input("Введите автора книги: ")

    while True:
        year = input("Введите год выпуска книги: ")

        if year.isdigit():
            book = Book(title, author, int(year))
            books = read_file()
            books.append({
                "book_id": book.book_id,
                "title": book.title,
                "author": book.author,
                "year": book.year,
                "status": book.status
            })
            write_file(books)
            return out_green_text("Книга добавлена!")

        else:
            print(exceptions_book_id)

def delete_book():
    """
    Удаление книги из файла JSON
    """

    books = read_file()
    if not books:
        return "Пока нет добавленных книг!\n"

    book_id = input("Введите ID книги которую хотите удалить: ")

    if book_id.isdigit():
        for book in books:
            if int(book["book_id"]) == int(book_id):
                books.remove(book)
                write_file(books)
                return out_green_text(f"Книга с book_id:{book_id} удалена.")

        else:
            return exceptions_book_found

    else:
        return exceptions_book_id

def search_book():
    """
    Поиск книги по автору, названию книги, году
    """

    books = read_file()
    if not books:
        return "Пока нет добавленных книг!"

    search_user = input("Поиск: ").strip()
    indicator = True
    for book in books:
        if any(map(lambda x: search_user in x, (book["author"], book["title"], str(book["year"])))):
            print(Book(**book))
            indicator = False
    if indicator:
        print("Книга с указанными параметрами не найдена!")

def views_books():
    """
    Вывод списка всех книг
    """

    books = read_file()
    if not books:
        print("Список книг пуст.")

    else:
        for num, value in enumerate(books, 1):
            print (f"{num}) {Book(**value)}")

def change_status():
    """
    Замена статуса (в наличии, выдана)
    """

    books = read_file()
    if not books:
        return "Пока нет добавленных книг!"

    book_id = input("Введите ID книги для изменения статуса: ")

    if book_id.isdigit():
        for book in books:
            if int(book_id) == book["book_id"]:
                book["status"] = "выдан" if book["status"] == "в наличии" else "в наличии"
            write_file(books)
            return out_green_text("Статус книги с ID:{} изменен!".format(book["book_id"]))
        return exceptions_book_found

    else:
        return exceptions_book_id
