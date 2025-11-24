class Cat:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

    def details(self):
        print(f"The cat is called {self.name} and it is {self.colour}")

bella = Cat("Bella", "blue")
sky = Cat("Sky", "black")
rory = Cat("Rory", "red")

bella.details()
sky.details()
rory.details()