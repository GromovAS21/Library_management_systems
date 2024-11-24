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
            books = read_file()
            books.append({
                "id": book.id,
                "title": book.title,
                "author": book.author,
                "year": book.year,
                "status": book.status
            })
            write_file(books)
            return out_green_text("Книга добавлена!")
        else:
            print(out_red_text("Введен некорректный год!"))

def delete_book():
    while True:
        books = read_file()
        if not books:
            return "Пока нет добавленных книг!\n"

        book_id = input("Введите ID книги которую хотите удалить: ")

        if book_id.isdigit():
            for book in books:
                if int(book["id"]) == int(book_id):
                    books.remove(book)
                    write_file(books)
                    return out_green_text(f"Книга с id:{book_id} удалена.")
            else:
                return "Книга c указанным ID не найдена!"
        else:
            print(out_red_text("Введен некорректный ID!"))

def search_book():
    """
    Поиск книги по автору, названию книги, году
    """
    books = read_file()
    if not books:
        return "Пока нет добавленных книг!"
    search_user = input("Поиск: ").strip()
    for book in books:
        if search_user in book["author"] or search_user in book["title"] or search_user in str(book["year"]):
            return Book(**book)
    return "Книга c указанным ID не найдена!"

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
    book_id = input("Введите id книги для изменения статуса: ")
    if book_id.isdigit():
        for book in books:
            if int(book_id) == book["id"]:
                if book["status"] == "в наличии":
                    book["status"] = "выдан"
                else:
                    book["status"] = "в наличии"
                write_file(books)
                return out_green_text("Статус книги с id {} изменен!".format(book["id"]))
        return "Книга c указанным ID не найдена!"
    else:
        print(out_red_text("Введен некорректный ID!"))
