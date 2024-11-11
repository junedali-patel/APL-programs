class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def display(self):
        return f"Brand: {self.brand}"

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def display(self):
        return f"Car - Brand: {self.brand}, Model: {self.model}"

class Bike(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def display(self):
        return f"Bike - Brand: {self.brand}, Model: {self.model}"

car = Car("Toyota", "Camry")
bike = Bike("Honda", "CBR250R")
print(car.display())   
print(bike.display())  
