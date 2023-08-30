
import math
from abc import ABCMeta,abstractmethod #to create abstract classes and methods

class Shape(metaclass=ABCMeta): #i want to make this class apstract 
                                #to prevent it from direct access 

    PI = math.pi  #CLASS Attribute 
    E = math.e

    @abstractmethod  # decorator to make the function abstract
    def area(self):     
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

    @staticmethod # to make the method static 
    @abstractmethod  # decorator to make the method abstract
    def calc_area(self):    # static method 
        pass
    
    @staticmethod
    @abstractmethod
    def calc_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return Circle.PI * self.radius ** 2
    
    def perimeter(self):
        return 2 * Circle.PI * self.radius
    
    @staticmethod
    def calc_area(radius):     
        return Circle.PI * radius ** 2

    @staticmethod
    def calc_perimeter(radius):
        return 2 * Circle.PI * radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    @staticmethod
    def calc_area(width, height):     
        return width * height

    @staticmethod
    def calc_perimeter(width, height):
        return 2 * (width + height)


class Triangle(Shape):
    def __init__(self, base, height, side1=None, side2=None):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2

        if self.height <= 0 or self.base <= 0:
            raise ValueError("height and base must be positive")

    def area(self):
        return 0.5 * self.base * self.height
    
    def perimeter(self):
        if self.side1 and self.side2:
            if self.side1 <= 0 or self.side2 <= 0:
                raise ValueError("All sides must be positive")
            return self.side1 + self.side2 + self.base
        
        print("warning, this works only on Equilateral Triangle")
        return 3 * self.base
    
    @staticmethod
    def calc_area(base, height):     
        return 0.5 * base * height

    @staticmethod
    def calc_perimeter(base, side1=None, side2=None):
        if side1 and side2:
            if side1 <= 0 or side2 <= 0:
                raise ValueError("All sides must be positive")
            return side1 + side2 + base
        
        print("warning, this works only on Equilateral Triangle")
        return 3 * base

    

def main():
    # instants, and instant methods
    circle = Circle(5)
    print("Circle Area:", circle.area())
    print("Circle Perimeter:", circle.perimeter())
    print('-'*50)

    rectangle = Rectangle(4, 6)
    print("Rectangle Area:", rectangle.area())
    print("Rectangle Perimeter:", rectangle.perimeter())
    print('-'*50)
    
    triangle = Triangle(3, 4)
    print("Triangle Area:", triangle.area())
    print("Triangle Perimeter:", triangle.perimeter())
    print('='*50)
# //////////////////////
# Class methods
    print("Circle Area:", Circle.calc_area(5))
    print("Circle Perimeter:", Circle.calc_perimeter(5))
    print('-'*50)
    
    print("Rectangle Area:", Rectangle.calc_area(4, 6))
    print("Rectangle Perimeter:", Rectangle.calc_perimeter(4, 6))
    print('-'*50)
    
    print("Triangle Area:", Triangle.calc_area(3, 4))
    print("Triangle Perimeter:", Triangle.calc_perimeter(3, 5,6))

if __name__ == "__main__":
    main()
