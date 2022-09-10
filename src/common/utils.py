import random
import string as string_lib


def _filter_generatable_char(generatable_char: str) -> str:
    not_allow_chars = "\"'"

    for char in not_allow_chars:
        generatable_char = generatable_char.replace(char, "")

    return generatable_char


def generate_random_str(
    n: int,
    alphabet_lower: bool = True,
    alphabet_upper: bool = True,
    digits: bool = True,
    punctuation: bool = True,
) -> str:
    letters = ""
    if alphabet_lower:
        letters += string_lib.ascii_lowercase
    if alphabet_upper:
        letters += string_lib.ascii_uppercase
    if digits:
        letters += string_lib.digits
    if punctuation:
        letters += string_lib.punctuation
    return "".join(random.choices(_filter_generatable_char(letters), k=n))
