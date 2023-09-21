from typing import TypeAlias

from constants import ___


Coordinates2D: TypeAlias = tuple[int, int]


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
