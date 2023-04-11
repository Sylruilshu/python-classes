
class Vehicle:

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

model = Vehicle(80, 250)

print(f"Max speed: {model.max_speed}, Mileage: {model.mileage}")