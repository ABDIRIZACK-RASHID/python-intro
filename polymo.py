import math

class Shape:
    def calculate_area(self):
        pass
class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def calculate_area(self):
        return self.width*self.height
class Circle(Shape):
    def __init__(self,radius):
        self.radius =radius
    def calculate_area(self):
        return math.pi*(self.radius**2)
def calculate_total_area(shape):
        totalarea=0
        for shape in shape:
            totalarea+=shape.calculate_area()
            return totalarea
mycircle=Circle(9)
myrectangle=Rectangle(5,7)
print(f"The area of the circle is {mycircle.calculate_area()}")
print(f"The area of the rectangle is {myrectangle.calculate_area()}")




