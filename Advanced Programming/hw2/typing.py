# hi



from typing import List, Dict, Tuple

pi: float = 3.14
nothing: str

myList: List[int] = [1, 2, 3]
myDict: Dict[str, int] = {'a': 1, 'b': 2, 'c': 3}
coord: Tuple[int, int, int] = (7, 12, 3)

coordinate_list: List[Tuple[int, int, int]]


def circumference(radius: float) -> float:
    return 2 * pi * radius


print(circumference(7.3))
print(circumference.__annotations__)
print(__annotations__)


def headline(text: str, align: bool = True) -> str:
    if align:
        return f"{text.title()}\n{'-' * len(text)}"
    else:
        f"{text.title()}".center(40, "*")


print(headline("This is a test", "center"))


class Book:

    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __len__(self):
        return self.pages


book = Book("Intro to Python", 827)
len(book)


def mylen(obj):
    return obj.__len__()


mylen(book)
mylen([1, 2, 3])
