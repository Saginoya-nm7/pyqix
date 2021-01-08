import dataclasses
import pygame
from pygame.math import Vector2


@dataclasses.dataclass
class Area:
    """複数点からなる多角形領域のクラス"""

    vertexes: list[Vector2]
    __size: float = dataclasses.field(init=False)

    def __post_init__(self):
        self.__size: float = self.__calcSize()

    def __calcSize(self) -> float:
        v = self.vertexes
        return abs(sum([(v[i].cross(v[(self.vertex_num if i == 0 else i) - 1])) for i in range(self.vertex_num)])) / 2

    @property
    def size(self) -> float:
        """領域の面積を返す

        :return: 領域の面積

        Example
        --------------------------
        >>> Area([Vector2(0,0),Vector2(1,0),Vector2(1,1),Vector2(0,1)]).size
        1.0
        >>> Area([Vector2(0,0),Vector2(1,0),Vector2(0,1)]).size
        0.5
        """
        return self.__size

    @property
    def vertex_num(self) -> int:
        return len(self.vertexes)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
