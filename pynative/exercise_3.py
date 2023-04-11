
class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass
    # def __init_(self, name, max_speed, mileage):
    #     super.__init__(name, max_speed, mileage)  <--- why dont we pass name, max_speed and mileage to our Vehicle init method to let that class handle those arguments?
                                                    #    Is it because we aren't creating any additional arguments for our Bus init?

school_bus = Bus("School Volvo", 60, 40)

print(f"Model: {school_bus.name}, Max speed: {school_bus.max_speed}, Mileage: {school_bus.mileage}")