class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi I'm {self.name} and I'm {self.age}.")


scott = Person("Scott", 49)
luna = Person("Luna", 6)

scott.introduce()
luna.introduce()