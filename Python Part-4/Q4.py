class Shape:
    def area(self):
        print("Area Method Called!")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(f"Area of Circle is {3.14*self.radius*self.radius}")

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        print(f"Area of Rectangle is {self.length*self.breadth}")

class Triangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width
    
    def area(self):
        print(f"Area of Triangle is {0.5*self.height*self.width}")

circle = Circle(5)
rectangle = Rectangle(5,5)
triangle = Triangle(4,5)

circle.area()
rectangle.area()
triangle.area()