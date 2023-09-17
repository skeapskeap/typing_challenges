from typing import TypeAlias

from constants import ___


Name: TypeAlias = str
Age: TypeAlias = int
Payments: TypeAlias = list[int]


def calculate_total_spent_for_user(user: tuple[Name, Age, Payments]) -> int:
    pass


if __name__ == "__main__":
    assert calculate_total_spent_for_user(user=("Ilya", 32, [102, 15, 63, 12])) == 192
