class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hi, I'm {self.name}")

class Customer(Person):
    def __init__(self, name, address):
        self.address = address
        super().__int__(name)

    def place_order(self, item):
        self.item = item

class Driver(Person):
    def __init__(self, name, vechile):
        self.vechile = vechile
        super().__int__(name)

    def deliver(self, order):
        print(f"{self.name} is delivering {self.item} to {self.customer} using {self.vechile}")

class DeliveryOrder:
    def __init__(self, customer ,item , status = "delivered"):
        self.item = item
        self.customer = customer
        self.status = status

    def assign_driver(driver):
        pass
        
    def summary(self):
        return """f
        Item: {self.item}
        Customer: {self.customer}
        Status: {self.status}
        Driver: {self.name}
        """
    
obj1 = Person("Alice")
obj1.introduce()
Order = DeliveryOrder("Alice", "Laptop", None)
Order.summary()