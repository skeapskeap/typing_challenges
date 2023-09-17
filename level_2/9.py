import datetime
from typing import TypeAlias

from constants import ___

ReceiptSerialNum: TypeAlias = int
PurchaseDate: TypeAlias = datetime
ProductName: TypeAlias = str
Amount: TypeAlias = int
Price: TypeAlias = float
Purchase = tuple[ProductName, Amount, Price]


def parse_receipt(raw_receipt: str) -> tuple[ReceiptSerialNum, PurchaseDate, list[Purchase]]:
    pass


if __name__ == "__main__":
    assert parse_receipt(
        raw_receipt="Кассовый чек 12 Продажа Позиции: ...",
    ) == (12, datetime.date(2022, 6, 12), [("Молоко", 1, 32.2)])
