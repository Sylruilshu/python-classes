
class Rectangle:

    # can you explicitly type hint like in other functions?
    def __init__(self, length, width):
        if length > 0:
            self.length = length
        else:
            self.length = None

        if width > 0:
            self.width = width
        else:
            self.width = None

    def perimeter(self):
        perimeter = (self.length + self.width) * 2
        return f"Perimeter: {perimeter}"
    
    def area(self):
        area = self.length * self.width
        return f"Area: {area}"

    def display(self):
        return f"Length: {self.length} \nWidth: {self.width} \n{self.perimeter()} \n{self.area()}"


class Parallelepiped(Rectangle):

    def __init__(self, length, width, height):
        super().__init__(length, width)
        if height > 0:
            self.height = height
        else:
            self.height = None

    def volume(self):
        volume = self.length * self.width * self.height
        return f"Volume: {volume} (assuming all angles are 90 degrees)"


rec = Rectangle(7, 5)
print(rec.display())
print("-----------------------------------------------")
para = Parallelepiped(7, 5, 2)
print(para.volume())
