def out_red_text(text) -> str:
    """
    Преобразовывает текст в курсив, красный цвет
    """

    return "\033[3m\033[5m\033[31m{}\033[0m".format(text)


def out_green_text(text) -> str:
    """
    Преобразовывает текст в курсив, зеленый цвет
    """

    return "\033[3m\033[5m\033[32m{}\033[0m".format(text)
