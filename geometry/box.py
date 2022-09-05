from dataclasses import dataclass
from geometry.point import Point


@dataclass
class Box:
    top_left: Point
    bottom_right: Point

    @property
    def left(self) -> float:
        return self.top_left.x

    @property
    def right(self) -> float:
        return self.bottom_right.x

    @property
    def top(self) -> float:
        return self.top_left.y

    @property
    def bottom(self) -> float:
        return self.bottom_right.y

    def copy(self) -> 'Box':
        return Box(self.top_left.copy(), self.bottom_right.copy())

    def contains(self, point: Point) -> bool:
        return self.top_left.x <= point.x <= self.bottom_right.x and self.top_left.y <= point.y <= self.bottom_right.y

    def intersect(self, box: 'Box') -> bool:
        return self._intersect(
            self.left, self.right, box.left, box.right) and self._intersect(
            self.top, self.bottom, box.top, box.bottom)

    def _intersect(self, x1: float, y1: float, x2: float, y2: float) -> bool:
        return x1 <= y2 and y1 >= x2

    @classmethod
    def create(cls, x1: float, y1: float, x2: float, y2: float) -> 'Box':
        return Box(Point(x1, y1), Point(x2, y2))
