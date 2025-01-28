# practicing usage of inheritance
"""
Exercise 1: Vehicle Hierarchy

Create a class hierarchy to represent different types of vehicles:

    Vehicle Class (Parent Class):
    -   Define properties brand and model that store the brand and model of the vehicle.
    -   Include a method get_info that returns a string in the format: "Brand: <brand>, Model: <model>".

    Car Class (Child Class):
    -   Inherit from the Vehicle class.
    -   Add an additional property num_doors to represent the number of doors in the car.
    -   Override the get_info method to include the number of doors in the output, like: "Brand: <brand>, Model: <model>, Doors: <num_doors>".

    Truck Class (Child Class):
    -   Inherit from the Vehicle class.
    -   Add an additional property load_capacity to represent the truck's load capacity in tons.
    -   Override the get_info method to include the load capacity in the output, like: "Brand: <brand>, Model: <model>, Load Capacity: <load_capacity> tons".

Your goal is to:

-   Understand how to design constructors in child classes by determining whether the parent class’s properties should be included in the child class’s constructor.
-   Use super() to call the parent class’s constructor to initialize shared properties (brand and model) while also handling the child-specific properties (num_doors or load_capacity).
"""
# parent class
class Vehicle:
    # constructor
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def get_info(self):
        return f"Brand: {self.brand}, Model: {self.model}"
    
# child class of vehicle
class Car(Vehicle):
    def __init__(self, brand, model, num_doors):
        # get property values from the parent 
        # parent's (vehicle) constructor
        super().__init__(brand, model)
        self.num_doors = num_doors

    def get_info(self):
        # get the existing info from the parent
        return super().get_info() + f", Doors: {self.num_doors}"
    
# child class of vehicle
class Truck(Vehicle):
    def __init__(self, brand, model, load_capacity):
        # get property values from the parent 
        # parent's (vehicle) constructor
        super().__init__(brand, model)
        self.load_capacity = load_capacity
    
    def get_info(self):
        # get the existing info from the parent
        return super().get_info() + f", Load Capacity: {self.load_capacity} tons"

# test cases
car = Car("Toyota", "Corolla", 4)
print(car.get_info())
# Result: Brand: Toyota, Model: Corolla, Doors: 4

truck = Truck("Ford", "F-150", 10)
print(truck.get_info())
# Result: Brand: Ford, Model: F-150, Load Capacity: 10 tons

car = Car("Honda", "Civic", 2)
print(car.get_info())
# Result: Brand: Honda, Model: Civic, Doors: 2

truck = Truck("Mercedes", "Actros", 25)
print(truck.get_info())
# Result: Brand: Mercedes, Model: Actros, Load Capacity: 25 tons

    
