from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x)
        print(self.y)

    def move(self, x1, y1):
        self.x += x1
        self.y += y1
        print(self.x)
        print(self.y)

    def distance(self, x1, y1):
        distance = str(sqrt(((self.x - x1)**2) + (self.y - y1)**2))
        print("Distance is: " + distance)


point = Point(0, 0)
point.show()
point.move(2, 3)
point.distance(4, 9)





