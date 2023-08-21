class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        pass

    def move(self):
        pass

    def display_info(self):
        print(f"{self.__class__.__name__}:")
        print("Name:", self.name)
        print("Age:", self.age)
        self.speak()
        self.move()
        print("-------------------------")


class Bird(Animal):
    def __init__(self, name, age, wingspan):
        super().__init__(name, age)
        self.wingspan = wingspan

    def speak(self):
        print("Bird says: Tweet!")

    def move(self):
        print("Bird flies.")

    def display_wingspan(self):
        print(f"Wingspan: {self.wingspan} inches")


class Fish(Animal):
    def __init__(self, name, age, water_type):
        super().__init__(name, age)
        self.water_type = water_type  # e.g., "Freshwater", "Saltwater"

    def speak(self):
        print("Fish says: Blub blub!")

    def move(self):
        print("Fish swims.")

    def display_water_type(self):
        print(f"Water type: {self.water_type}")


# Example usage
parrot = Bird("Polly", 5, 12)
salmon = Fish("Sammy", 3, "Freshwater")

parrot.display_info()
parrot.display_wingspan()

salmon.display_info()
salmon.display_water_type()
