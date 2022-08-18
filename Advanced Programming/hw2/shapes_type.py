from shapes import Shape, Circle


def print_area(something):
    if isinstance(something, Shape):
        # type(something) == Shape will not work
        print(f'the area of this {something.kind} is {something.area()}')
    else:
        print("I have no idea what you mean")


def get_area_of_shape(shape: Shape) -> float:
    area = shape.area()
    print(area)
    return area


class Cookie:
    pass