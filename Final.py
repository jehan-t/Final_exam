class Person:
    def __int__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hi, I'm {self.name}")


class Customer(Person):
    def __init__(self, name, address):
        self.address = address
        super().__int__(name)

    def place_order(self, item):
        return DeliveryOrder()

class Driver(Person):
    def __init__(self, name, vechile):
        self.vechile = vechile
        super().__int__(name)

    def deliver(self, order):
        print(f"{self.name} is delivering {self.item} to {self.customer} using {self.vechile}")


class DeliveryOrder:
    def __init__(self, customer ,item , status = True):
        self.item = item
        self.customer = customer
        self.status = status


    def assign_driver(driver):
        pass
        

    def summary(self):
        return f"{self.customer} , {self.item}, "