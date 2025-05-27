class vehicle:
    def __init__(self,name,speed,mileage):
        self.name=name
        self.speed=speed
        self.mileage=mileage

class car(vehicle):
    pass

c1=car("Benz",200,15)

print(c1.name)
print(c1.speed)
print(c1.mileage)