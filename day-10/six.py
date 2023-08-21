class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display(self):
        print(f"Make: {self.make}, Model: {self.model}")


class Car(Vehicle):
    def __init__(self, make, model, seats):
        super().__init__(make, model)
        self.seats = seats


class Bike(Vehicle):
    pass  # Assume no additional attributes for simplification


class Truck(Vehicle):
    pass  # Assume no additional attributes for simplification


# Example
car = Car("Toyota", "Camry", 5)
car.display()
