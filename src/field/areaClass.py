from src.util import Vec2


class Area:

    def __init__(self, vertex_list: list[Vec2]):
        """複数点からなる多角形領域のクラス
        """
        self.__vertexes: list[Vec2] = vertex_list
        self.__size: float = self.__calcSize()

    def __calcSize(self) -> float:
        v = self.__vertexes
        return abs(sum([(v[i] @ v[(i if i != 0 else self.vertice_num) - 1]).abs for i in range(self.vertice_num)])) / 2

    @property
    def size(self) -> float:
        """領域の面積を返す

        :return: 領域の面積

        Example
        --------------------------
        >>> Area([Vec2(0,0),Vec2(1,0),Vec2(1,1),Vec2(0,1)]).size
        1.0
        >>> Area([Vec2(0,0),Vec2(1,0),Vec2(0,1)]).size
        0.5
        """
        return self.__size

    @property
    def vertice_num(self) -> int:
        return len(self.__vertexes)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
