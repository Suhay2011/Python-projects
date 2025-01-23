class Vehicle:

    def __init__(self,name,max_speed,mileage):
        self.name = nameself.max_speed = max_speedself.mileage = mileage
    class Bus(Vehicle):
        pass

School_bus = Bus("School Volvo" ,180, 12)
print("Vehicle Name:" ,School_bus.name ,"speed:",School_bus.max_speed,
"Mileage:", School_bus.mileage)
