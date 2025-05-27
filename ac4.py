class vehicles:
    def __init__(self):
        print("Its a parent class")

class bus(vehicles):
    def __init__(self):
        vehicles.__init__('bus')


print(issubclass(bus,vehicles))
print(issubclass(bus,bus))
print(issubclass(bus,list))
    