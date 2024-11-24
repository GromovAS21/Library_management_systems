class Book:
    """
    Класс книги
    """
    book_id = 1

    def __init__(self, title:str, author:str, year:int, id=None, status="в наличии"):
        self.id = Book.book_id if id is None else id
        self.title = title
        self.author = author
        self.year = year
        self.status = status
        Book.book_id += 1

    def __repr__(self):
        return f"{self.__class__.__name__}({self.id}, {self.title}, {self.author}, {self.year}, {self.status})"