
class Geometry:

    def __init__(self):
        self.shape = "Tesseract"

    def distance(self, x, y, a, b):
        m = (b -y) + (a -x)
        return m

shape = Geometry()

print(shape.distance(0,0,4,0))