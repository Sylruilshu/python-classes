
class Vehicle:

    colour = "white"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass


bus = Bus("School Volvo", 100, 12)
car = Car("Audi Q5", 240, 18)

print(f"Colour: {bus.colour}, Vehicle name: {bus.name}, Max Speed: {bus.max_speed}, Mileage: {bus.mileage}")
print(f"Colour: {car.colour}, Vehicle name: {car.name}, Max Speed: {car.max_speed}, Mileage: {car.mileage}")