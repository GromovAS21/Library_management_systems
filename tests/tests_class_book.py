from unittest import TestCase

from class_books import Book


class TestBook(TestCase):
    """
    Тесты класса Book
    """

    def setUp(self):

        self.book_1 = Book("Книга_1", "Автор_1", 2000)
        self.book_2 = Book("Книга_2", "Автор_2", 2010, book_id=100)

    def test_book(self):
        """
        Проверка инициализации экземпляра класса Book
        """

        self.assertEqual(self.book_1.book_id, 1)
        self.assertEqual(self.book_1.title, "Книга_1")
        self.assertEqual(self.book_1.author, "Автор_1")
        self.assertEqual(self.book_1.year, 2000)
        self.assertEqual(self.book_2.book_id, 100)


if __name__ == "__main__":
    TestBook()