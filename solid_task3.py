# Задача 3. Принцип подстановки Лисков (LSP)
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height


class Square(Shape):
    def __init__(self, size):
        self.size = size
        
    def area(self):
        return self.size ** 2


def print_area(shape: Shape):
    print(f"Area: {shape.area()}")