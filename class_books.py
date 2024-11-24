class Book:
    """
    Класс книги
    """
    book_id = 1

    def __init__(self, title:str, author:str, year:int, id=None, status="в наличии"):
        self.__id = self.book_id if id is None else id
        self.__title = title
        self.__author = author
        self.__year = year
        self.__status = status
        Book.book_id += 1

    def __str__(self):
        """
        Строчное представление класса
        """

        return "id:{} {}-{}, {} г. ({})".format(self.__id, self.__title, self.__author, self.__year, self.__status)