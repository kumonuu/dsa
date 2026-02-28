# polymorphism

# python has in-built polymorphism
class Fruit:
    def method(self):
        print("fruit")

class Car:
    def method(self):
        print("vroom")

# if python doesn't support polymorphism
def function(arg):
    if isinstance(arg,Fruit):
        arg.method()
    if isinstance(arg,Car):
        arg.method()

fruit = Fruit()
car = Car()

fruit.method()
car.method()

function(fruit)
function(car)