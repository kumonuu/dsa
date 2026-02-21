# object oriented programming

class Fruit:
    def __init__(self,color,taste,shape):
        self.color = color
        self.taste = taste
        self.shape = shape
    def get_shape(self):
        return self.shape
    def set_shape(self, shape):
        self.shape = shape
    def show_fruit(self):
        print(self)

orange = Fruit("orange","sweet","sphere")
print(orange.get_shape())
orange.set_shape("triangle")
print(orange.get_shape())
orange.show_fruit()