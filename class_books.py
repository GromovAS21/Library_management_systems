class Book:
    """
    Класс книги
    """
    BOOK_ID = 0

    def __init__(self, title:str, author:str, year:int, id=None, status="в наличии"):
        self.id = self.set_book_id() if id is None else id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def __repr__(self):
        return f"{self.__class__.__name__}({self.id}, {self.title}, {self.author}, {self.year}, {self.status})"

    @classmethod
    def set_book_id(cls):
        cls.BOOK_ID += 1
        return cls.BOOK_ID