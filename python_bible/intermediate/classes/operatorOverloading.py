# OPERATOR OVERLOADING

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "X: %d, Y: %d" % (self.x,
                                 self.y)

    def __add__(self, other):
        return Vector(self.x + other.x,
                      self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x,
                      self.y - other.y)


v1 = Vector(3, 5)
v2 = Vector(6, 2)
v3 = v1 + v2
v4 = v1 - v2
print(v1)
print(v2)
print(v3)
print(v4)
