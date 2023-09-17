from typing import TypeAlias

from constants import ___

Code: TypeAlias = str


def is_recovery_code_correct(code: Code, user_codes: list[Code]) -> bool:
    pass


if __name__ == "__main__":
    assert is_recovery_code_correct(code="5212", user_codes=["1862", "8172", "7212"]) is False
