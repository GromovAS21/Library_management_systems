from services import out_red_text
from src import adding_book, change_status, delete_book, search_book, views_books


def main():
    while True:
        input_user = input("\nВведите команду: ").lower().strip()
        if input_user == "list":
            views_books()
        elif input_user == "add":
            print(adding_book())
        elif input_user == "delete":
            print(delete_book())
        elif input_user == "search":
            search_book()
        elif input_user == "change":
            print(change_status())
        elif input_user == "stop":
            print("Программа завершена.")
            break
        else:
            print(out_red_text("Неизвестная команда!"))


if __name__ == "__main__":
    main()

