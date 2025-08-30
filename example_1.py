class Circle:                                                  
    def __init__(self, radius):                                 
        self.radius = radius

    def area(self):
        pi = 3.14159
        return pi * (self.radius**2)

radius = float(input('Enter radius to find area of circle: '))
circl = Circle(radius)
print(f'Area of circle is {circl.area()}')