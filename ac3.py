class bird:
    def __init__(self):
        print("Its a bird")
    def swim(self):
        print("Faster swimmer")


class flamingo(bird):
    def __init__(self):
        super().__init__()
    def migrate(self):
        print("Migratory bird")

obj=flamingo()
obj.swim()
obj.migrate()