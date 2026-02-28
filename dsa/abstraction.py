# abstraction

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    pass
    #def area(self):
        #pass

rect = Rectangle()