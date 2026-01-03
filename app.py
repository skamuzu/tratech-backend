class Vehicle():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def get_info(self):
        return f"{self.year} {self.make} {self.model}"
    
car = Vehicle("Toyota", "Camry", 2020)
print(car.get_info())  