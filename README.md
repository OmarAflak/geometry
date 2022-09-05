# Point

This is a helper class to work with 2D points.

```python
from point.point import Point

a = Point(3, 4)
b = Point(1, 6)
c = 2 * a.rotate(3.14 / 2) + b.unit().dot(a)
```

# Install

```
python -m pip install git+https://github.com/omaraflak/point 
```