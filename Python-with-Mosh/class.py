class Point:

    def __init__(self, x, y):  # Constructor
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("Draw")

point = Point(4, 5,)

print(point.x)
