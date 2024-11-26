class Book:
    """
    Класс книги
    """

    __BOOK_ID = 0

    __slots__ = ("__title", "__author", "__year", "__book_id", "__status")

    def __init__(self, title: str, author: str, year: int, book_id=None, status="в наличии"):
        self.__book_id = self.set_book_id() if book_id is None else book_id
        self.__title = title
        self.__author = author
        self.__year = year
        self.__status = status

    def __repr__(self):
        """
        Отладочный вывод экземпляра
        """

        return f"{self.__class__.__name__}({self.__book_id}, {self.__title}, {self.__author}, {self.__year}, {self.__status})"

    def __str__(self):
        """
        Клиентский вывод экземпляра
        """

        return f"id:{self.__book_id} {self.__title}-{self.__author}, {self.__year} г. ({self.__status})"

    @classmethod
    def set_book_id(cls):
        """
        Увеличение ID для создания других объектов
        """

        cls.__BOOK_ID += 1
        return cls.__BOOK_ID

    @property
    def get_id(self):
        """
        Вывод ID книги
        """

        return self.__book_id

    @property
    def get_title(self):
        """
        Вывод названия книги
        """

        return self.__title

    @property
    def get_author(self):
        """
        Вывод автора
        """

        return self.__author

    @property
    def get_year(self):
        """
        Вывод года
        """

        return self.__year

    @property
    def get_status(self):
        """
        Вывод статуса
        """

        return self.__status

    @classmethod
    def create_book(cls, title: str, author: str, year: int, book_id=None, status="в наличии"):
        """
        Создание экземпляра Book
        """
        return cls(title, author, year, book_id, status)

