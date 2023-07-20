# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#     def Area(self):
#         area=3.14*radius*radius
#         print(area)
#     def Perimeter(self):
#         peri=2*3.14*radius
#         print(peri)

# instance=Circle(radius)

# radius=input("Enter the radius: ")
# instance.Area()
# instance.Perimeter()

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def Area(self):
        return math.pi * self.radius**2

    def Perimeter(self):
        return 2 * math.pi * self.radius

radius = float(input("Enter the radius: "))
circle = Circle(radius)

print(f"Area: {circle.Area()}")
print(f"Perimeter: {circle.Perimeter()}")
