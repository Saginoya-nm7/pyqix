import dataclasses
import math


@dataclasses.dataclass
class Vec2:
    """2次元のベクトル
    
    """
    x: float
    y: float
    abs: float = dataclasses.field(init=False)

    def __post_init__(self):
        self.abs = math.sqrt(self.x ** 2 + self.y ** 2)

    def __abs__(self) -> float:
        """ベクトルの絶対値

        :return: 絶対値

        Example
        --------------------
        >>> abs(Vec2(5,12))
        13.0

        >>> abs(Vec2(-3,4))
        5.0
        """
        return self.abs

    def __add__(self, other: "Vec2") -> "Vec2":
        """ベクトルどうしの足し算

        Example
        --------------------
        >>> Vec2(3,5) + Vec2(4,8) == Vec2(7,13)
        True

        >>> Vec2(3,5) + Vec2(-4,-8) == Vec2(-1,-3)
        True
        """

        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vec2") -> "Vec2":
        """ベクトルどうしの引き算

        Example
        --------------------
        >>> Vec2(3,5) - Vec2(4,8) == Vec2(-1,-3)
        True

        >>> Vec2(3,5) - Vec2(-4,-8) == Vec2(7,13)
        True
        """

        return Vec2(self.x - other.x, self.y - other.y)

    def __mul__(self, other: "Vec2") -> float:
        """ベクトルどうしの内積をとる

        Example
        --------------------
        >>> Vec2(3,5) * Vec2(4,8)
        52

        >>> Vec2(0,0) * Vec2(5,8)
        0
        """

        return self.x * other.x + self.y * other.y

    def __matmul__(self, other: "Vec2") -> "Vec3":
        """ベクトルどうしの外積をとる

        Example
        ---------------
        >>> Vec2(3,4) @ Vec2(5,6)
        Vec3(x=0, y=0, z=-2, abs=2.0)

        >>> Vec2(5,0) @ Vec2(0,5)
        Vec3(x=0, y=0, z=25, abs=25.0)

        >>>
        """
        return Vec3(0, 0, self.x * other.y - self.y * other.x)


@dataclasses.dataclass
class Vec3:
    """3次元のベクトル

    """
    x: float
    y: float
    z: float
    abs: float = dataclasses.field(init=False)

    def __post_init__(self):
        self.abs = math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __abs__(self):
        """ベクトルの絶対値

        :return: 絶対値

        Example
        ---------------
        >>> abs(Vec3(3,4,0))
        5.0

        >>> abs(Vec3(5,0,12))
        13.0

        >>> abs(Vec3(0,8,15))
        17.0

        """

        return self.abs

    def __add__(self, other: "Vec3") -> "Vec3":
        """3次元ベクトルの足し算

        :return: 演算結果

        Example
        --------------------
        >>> Vec3(1,2,3) + Vec3(4,5,6) == Vec3(5,7,9)
        True

        >>> Vec3(1,-2,3) + Vec3(-4,5,-6) == Vec3(-3,3,-3)
        True
        """

        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: "Vec3") -> "Vec3":
        """3次元ベクトルの足し算

        :return: 演算結果

        Example
        --------------------
        >>> Vec3(1,2,3) - Vec3(4,5,6) == Vec3(-3,-3,-3)
        True

        >>> Vec3(1,-2,3) - Vec3(-4,5,-6) == Vec3(5,-7,9)
        True
        """

        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
