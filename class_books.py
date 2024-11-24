class Book:
    """
    Класс книги
    """
    book_id = 1
    def __init__(self, title:str, author:str, year:int, status="в наличии"):
        self.id = self.book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status
        Book.book_id += 1

    def __str__(self):
        """
        Строчное представление класса
        """

        return "{}. {} - {}, {} г. {}".format(self.id, self.title, self.author, self.year, self.status)

