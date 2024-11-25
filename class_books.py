class Book:
    """
    Класс книги
    """

    BOOK_ID = 0

    __slots__ = ("title", "author", "year", "id", "status")

    def __init__(self, title:str, author:str, year:int, id=None, status="в наличии"):
        self.id = self.set_book_id() if id is None else id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def __repr__(self):
        """
        Отладочный вывод экземпляра
        """
        return f"{self.__class__.__name__}({self.id}, {self.title}, {self.author}, {self.year}, {self.status})"

    def __str__(self):
        """
        Клиентский вывод экземпляра
        """
        return f"id:{self.id} {self.title}-{self.author}, {self.year} г. ({self.status})"

    @classmethod
    def set_book_id(cls):
        """
        Увеличение ID для создания других объектов
        """
        cls.BOOK_ID += 1
        return cls.BOOK_ID