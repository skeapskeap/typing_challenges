from typing import TypeAlias

from constants import ___


PositionX: TypeAlias = int
PositionY: TypeAlias = int
Coordinates2D: TypeAlias = tuple[PositionX, PositionY]


def is_point_in_square(point: Coordinates2D,
                       left_upper_corner: Coordinates2D,
                       right_bottom_corner: Coordinates2D) -> bool:
    pass


if __name__ == "__main__":
    assert is_point_in_square(
        point=(10, 12),
        left_upper_corner=(5, 5),
        right_bottom_corner=(20, 15)
    ) is True
