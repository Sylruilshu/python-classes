
class Vehicle:
    
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):

    def seating_capacity(self, capacity=50):
        return f"The seating capacity of a {self.name} is {capacity} passengers"
        # They have: return super().seating_capacity(capacity=50) <--- Why? does it just save having to rewrite f"The seating capacity of a {self.name} is {capacity} passengers"


school_bus = Bus("School Volvo", 60, 40)

print(school_bus.seating_capacity())

