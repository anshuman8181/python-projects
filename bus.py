class Vehicle:

    def __init__(self,name,max_speed,milage):
        self.name = name
        self.max_speed = max_speed
        self.milage = milage
    
class Bus(Vehicle):
    pass

School_bus = Bus("school Volvo",180, 12)
print("Vehicle Name:",School_bus.name,"Speed:",School_bus.max_speed,"milage",
      School_bus.milage)
