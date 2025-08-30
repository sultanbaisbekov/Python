class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def perimeter(self):
        return 2 * (self.width + self.length)
    
    def area(self):
        return self.width * self.length
    
width = float(input('Enter a width: '))
length = float(input('Enter a length: '))

rectangle = Rectangle(width, length)

print(f'Perimeter of rectangle is {rectangle.perimeter()}')
print(f'Area of rectangle is {rectangle.area()}')