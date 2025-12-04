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
    def __init__(self, name, vechile, item, customer):
        self.vechile = vechile
        self.item = item
        self.customer = customer
        super().__init__(name)

    def deliver(self):
        print(f"{self.name} is delivering {self.item} to {self.customer} using {self.vechile}.")

    def Final_status(self):
        print(f"Order for {self.item} is delivered")

class DeliveryOrder:
    def __init__(self, customer ,item , driver ,status = "delivered",):
        self.item = item
        self.customer = customer
        self.status = status
        person = Person(driver)
        self.driver = person.name

    def assign_driver(driver):
        pass
        
    def summary(self):
        return f"Item: {self.item}\nCustomer: {self.customer}\nStatus: {self.status}\nDriver: {self.driver}"
   
obj1 = Person("Alice")
obj2 = Person("Bob")
obj3 = Person("David")
obj1.introduce()
obj2.introduce()
obj3.introduce()
print()
Order1 = DeliveryOrder("Alice", "Laptop", "David", "preparing")
print("Order Summary: ")
print(Order1.summary())
print()
Order2 = DeliveryOrder("Bob", "Headphone", "Daivid", "preparing")
print("Order Summary: ")
print(Order2.summary())
print()
drv1 = Driver("David", "motorcycle", "Laptop", "Alice")
drv2 = Driver("David", "motorcycle", "Headphones", "Bob")
drv1.deliver()
drv2.deliver()
print()
print("Final Status:")
drv1.Final_status()
drv2.Final_status()