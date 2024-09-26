# main.py

def remainder(dividend, divisor):
    """
    Вычисляет остаток от деления dividend на divisor.

    :param dividend: делимое
    :param divisor: делитель
    :return: остаток от деления
    :raises ValueError: если делитель равен нулю
    """
    if divisor == 0:
        raise ValueError("Деление на ноль недопустимо")
    return dividend % divisor