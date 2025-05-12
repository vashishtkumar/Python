import math

class Circle:
    def __init__(self,radius):
        self.radius=radius

    def Area(self):
        return math.pi*self.radius*self.radius
    
    def Perimeter(self):
        return 2*math.pi*self.radius
    


C1=Circle(4)

print(f"The area of circle is {C1.Area()} And its Perimeter is {C1.Perimeter}")