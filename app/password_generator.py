import random

def password_generator(
        length: int = 15,
        upper: bool = True,
        lower: bool = True,
        nums: bool = True,
        syms: bool = True
        ):

    UPPERCASE = "ABCDEFGHIJKLMLOPQRSTUVWXYZ"
    LOWERCASE = UPPERCASE.lower()
    DIGITS = "0123456789"
    SYMBOLS = "@#$%^&*()"

    base_string = ""

    if upper:
        base_string += UPPERCASE

    if lower:
        base_string += LOWERCASE

    if nums:
        base_string += DIGITS

    if syms:
        base_string += SYMBOLS

    length = 15

    return "".join(random.sample(base_string, length))
