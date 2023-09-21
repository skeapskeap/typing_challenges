import decimal
from typing import Mapping, TypeAlias

from constants import ___

TrId: TypeAlias = int
TrAmount: TypeAlias = decimal.Decimal


def get_transaction_amount(transaction_id: TrId,
                           transactions_amounts_map: Mapping[TrId, TrAmount]) -> TrAmount:
    pass


if __name__ == "__main__":
    transactions_amounts_map = {
        156: decimal.Decimal("30.6"),
        514: decimal.Decimal("164.1"),
        372: decimal.Decimal("92"),
    }
    assert get_transaction_amount(transaction_id=156, transactions_amounts_map=transactions_amounts_map) == decimal.Decimal("30.6")
    assert get_transaction_amount(transaction_id=1000, transactions_amounts_map=transactions_amounts_map) is None
