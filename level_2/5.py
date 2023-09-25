from typing import NamedTuple

from constants import ___


class User(NamedTuple):
    full_name: str
    age: int
    email: str


def get_current_user() -> User:
    pass


if __name__ == "__main__":
    assert get_current_user() == ("Ilya Lebedev", 33, "melevir@gmail.com")
