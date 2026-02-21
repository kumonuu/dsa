class Car:
    def __init__(self,brand,fuel,model,color):
        self.brand = brand
        self.fuel = fuel
        self.model = model
        self.color = color
    def show_details(self):
        print("Brand: " + self.brand)
        print("Fuel: " + str(self.fuel) + " litres")
        print("Model: " + self.model)
        print("Color: " + self.color)

class SUV(Car):
    def __init__(self,brand,fuel,model,color,year,transmission):
        Car.__init__(self,brand,fuel,model,color)
        self.year = year
        self.transmission = transmission
    def show_details(self):
        Car.show_details(self)
        print("Year: " + str(self.year))
        print("Transmission: " + self.transmission)

suv = SUV("brand",30,"model","blue",1998,"automatic")
suv.show_details()