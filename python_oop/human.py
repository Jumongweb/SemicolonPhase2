class Human:
    numbers_of_eyes = 2

    def __init__(self, height: float, gender: str, name: str):
        self.height = height
        self.gender = gender
        self.name = name

    def sleep(self):
        print("Sleeping......")

    def eat(self):
        print(f"{self.name} eating.....")

    def __str__(self):
        return f"{self.name} {self.gender}"


h1 = Human(4.1, "male", "Bolaji")
h2 = Human(3.8, "female", "Hannah")

# Dundar method
print(h1)
print(h1.height)
print(h2.eat())
print(h1.eat())
print(type(h1))
print(h2.numbers_of_eyes)
