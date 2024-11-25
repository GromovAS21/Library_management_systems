from unittest import TestCase

from services import out_red_text, out_green_text


class TestServices(TestCase):
    """
    Тесты для сервисных функций
    """

    def test_out_red_text(self):
        """
        Тест функции out_red_text
        """

        self.assertEqual(out_red_text("Test"), "\x1b[3m\x1b[5m\x1b[31mTest\x1b[0m")

    def test_out_green_text(self):
        """
        Тест функций out_green_text
        """

        self.assertEqual(out_green_text("Test"), "\x1b[3m\x1b[5m\x1b[32mTest\x1b[0m")