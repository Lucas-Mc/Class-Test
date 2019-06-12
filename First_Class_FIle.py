# Lucas McCullum
# June 12, 2019

# Python class tetsing

### First Test ###
# class Rectangle:

#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

#     def perimeter(self):
#         return 2 * self.length + 2 * self.width

# # Here we declare that the Square class inherits from the Rectangle class
# class Square(Rectangle):

#     def __init__(self, length):
#         super().__init__(length, length)

# square = Square(4)
# print(square.area())

### Second Test ###
class Square(Rectangle):

    def __init__(self, length):
        super().__init__(length, length)

class Cube(Square):
    
    def surface_area(self):
        face_area = super().area()
        return face_area * 6

    def volume(self):
        face_area = super().area()
        return face_area * self.length

cube = Cube(3)
print(cube.surface_area())
print(cube.volume())





