import math
from dataclasses import dataclass
from random import randrange
from typing import Optional


@dataclass
class Point:
    x: float = 0
    y: float = 0

    def length(self) -> float:
        """
        Magnitude of the vector

        @return: L2 distance
        """
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def unit(self) -> 'Point':
        """
        Scale vector to make its length one

        @return: vector of length 1 whose direction is unchanged
        """
        return self / self.length()

    def distance_to(self, other: 'Point') -> float:
        """
        Distance to another point

        @param other: point to measure the distance to
        @return: L2 distance to `other`
        """
        return (self - other).length()

    def angle_to(self, other: 'Point') -> float:
        """
        Angle to another vector in [-pi, pi]

        @param other: point to measure the angle to
        @return: angle in radians
        """
        return math.atan2(other.y, other.x) - math.atan2(self.y, self.x)

    def rotate(
        self,
        angle: float,
        around: Optional['Point'] = None
    ) -> 'Point':
        """
        Rotate point by angle around another one

        @param angle: angle of the rotation in radians
        @param around: optional point to rotate about
        """
        around = around or Point()
        tmp = self - around
        return around + Point(
            tmp.x * math.cos(angle) - tmp.y * math.sin(angle),
            tmp.x * math.sin(angle) + tmp.y * math.cos(angle)
        )

    def dot(self, other: 'Point') -> float:
        """
        Computes dot product

        @param other: vector to compute the dot product with
        @return: dot product as `x1 * x2 + y1 * y2`
        """
        return self.x * other.x + self.y * other.y

    def bound(self, x_min: float, x_max: float, y_min: float, y_max: float):
        """
        Bound x and y coordinates so that if they exceed their bound they will wrap around the provided window.

        @param x_min: lower bound for x
        @param x_max: upper bound for x
        @param y_min: lower bound for y
        @param y_max: upper bound for y
        """
        if self.x > x_max:
            self.x = x_min
        if self.x < x_min:
            self.x = x_max
        if self.y > y_max:
            self.y = y_min
        if self.y < y_min:
            self.y = y_max

    def set_length(self, length: float):
        """
        Set the magnitude of the vector, i.e. value returned by `length()`

        @param length: new magnitude
        """
        self.mul(length / self.length())

    def limit_length(self, max_length: float):
        """
        Set the magnitude of the vector to the value provided if it exceeds it

        @param length: limit magnitude
        """
        length = self.length()
        if length > max_length:
            self.set_length(max_length)

    def is_zero(self) -> bool:
        """
        Check if this point is the origin

        @return: Returns `True` if x and y are both 0, `False` otherwise
        """
        return self.x == 0 and self.y == 0

    def copy(self) -> 'Point':
        """
        Create a copy of the point

        @return: copy of current point
        """
        return Point(self.x, self.y)

    def set(self, other: 'Point') -> 'Point':
        """
        Set the value of x and y from another point

        @param other: point to get the values from
        @return: reference to the current point 
        """
        self.x = other.x
        self.y = other.y
        return self

    def add(self, other: 'Point') -> 'Point':
        """
        Add the value of x and y from another point

        @param other: point to get the values from
        @return: reference to the current point 
        """
        self.x += other.x
        self.y += other.y
        return self

    def sub(self, other: 'Point') -> 'Point':
        """
        Subtract the value of x and y from another point

        @param other: point to get the values from
        @return: reference to the current point 
        """
        self.x -= other.x
        self.y -= other.y
        return self

    def mul(self, other: float) -> 'Point':
        """
        Multiply x and y by a scalar

        @param other: scalar value
        @return: reference to the current point 
        """
        self.x *= other
        self.y *= other
        return self

    def div(self, other: float) -> 'Point':
        """
        Divide x and y by a scalar

        @param other: scalar value
        @return: reference to the current point 
        """
        return self.mul(1 / other)

    def __add__(self, other: 'Point') -> 'Point':
        return self.copy().add(other)

    def __sub__(self, other: 'Point') -> 'Point':
        return self.copy().sub(other)

    def __mul__(self, other: float) -> 'Point':
        return self.copy().mul(other)

    def __rmul__(self, other: float) -> 'Point':
        return self.copy().mul(other)

    def __truediv__(self, other: float) -> 'Point':
        return self.copy().div(other)

    def __neg__(self) -> 'Point':
        return Point().sub(self)

    @classmethod
    def random(cls, x_range: range, y_range: range) -> 'Point':
        return Point(
            randrange(x_range.start, x_range.stop, x_range.step),
            randrange(y_range.start, y_range.stop, y_range.step)
        )
