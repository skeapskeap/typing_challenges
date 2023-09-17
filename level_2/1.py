from typing import TypeAlias

from constants import ___

Rate: TypeAlias = float


def get_avg_currency_rate(rates_history: list[Rate]) -> Rate:
    pass


if __name__ == "__main__":
    assert get_avg_currency_rate(rates_history=[30.2, 31.6, 29.0]) == 30.3
