import math


class ShapeFactory:

    def get_shape(self, shape_type, **kwargs):
        if shape_type == 'circle':
            return Circle(name = kwargs['name'], radius = kwargs['radius'])
        elif shape_type = 'square':
            return Square(name = kwargs['name'], side=kwargs['side'])
        else:
            return None

class ShapeType:
    SQUARE ='square'
    CIRCLE='circle'

factory = ShapeFactory()
sq = factory.get_shape(ShapeType.SQUARE, name='mysquare',size=10)
c = factory.get_shape(ShapeType.CIRCLE, name='mycircle', radius=10)
c = Circle('circle of lifeee', 10)


class ShapeException(Exception):
    pass

class InvalidShape(ShapeException):
    pass

class OutOfShape(ShapeException):
    pass


def add(x, *args):
    return sum(args) + x


def add(x, **kwargs):
    print(x)
    for k, w in kwargs.items():
        print(k, w)




class Shape:
    kind = 'shape'  # a calls attribute shared by all instances
    num = 0

    def __init__(self, name, xpos=0, ypos=0):
        self.name = name
        self.xpos = xpos
        self.ypos = ypos

        Shape.num += 1

    def get_position(self):
        return self.xpos, self.ypos

    def move(self, dx, dy):
        self.xpos += dx
        self.ypos += dy

    def __repr__(self):
        return F"{self.name} ({self.kind} {self.get_position()})"


class Circle(Shape):
    kind = 'circle'
    num = 0

    def __init__(self, name, radius, xpos=0, ypos=0):
        super().__init__(name, xpos, ypos)
        self.radius = radius
        Circle.num += 1

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius


class ResizeCircle(Circle):
    kind = "resizeable circle"
    num = 0

    def __init__(self, name, radius):
        super().__init__(name, radius)
        ResizeCircle.num += 1

    def set_radius(self: Circle, radius: float) -> None:
        self.radius = radius


def main():
    blob = Shape('blob')
    print(blob)
    print(Shape.num)

    c1 = Circle("circle", 10)
    print(c1.area())

    rc = ResizeCircle("stretchy", 12)
    rc.set_radius(13)
    print(Shape.num)


for shape_class in [Shape, Circle, ResizeCircle]:
    print(shape_class.kind + 's', shape_class.num)

if __name__ == "__main__":
    main()
