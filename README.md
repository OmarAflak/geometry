# Geometry

This is a simple geometry library for Python.

```python
from geometry.point import Point

a = Point(3, 4)
b = Point(1, 6)
c = 2 * a.rotate(3.14 / 2) + b.unit().dot(a)
```

# Install

```
python -m pip install git+https://github.com/omaraflak/geometry
```