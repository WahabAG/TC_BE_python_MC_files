# Inheritance

# # syntax
# class Parent:
#     def greet(self):
#         print(f"HELLO WORLD")

# class Child(Parent):
#     pass

# # subInheritance
# class specificChild(Child):
#     pass

# child_obj = Child()
# child_obj.greet()

# specificChild_obj = specificChild()
# specificChild_obj.greet()

# """Using the super() key word"""
# # example

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def sound(self):
#         print("Animals Makes sounds")


# class Dog(Animal):

#     def __init__(self, name, breed):
#         super().__init__(name) # accessing the parent class
#         self.breed = breed  # adding new method to child class
#         self.color = "white black stripes"

#     def sound(self):
#         print(f"{self.name} barks!!")

#     def height(self):
#         return "3 meters"
    
#     def color(self, color):
#         self.color = color
#         print(f"{self.name} barks!!")

# dog = Dog("Trex", "Husky")
# dog.sound()
# print(dog.height())

# inheritance class task
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats

    def car_details(self):
        print(f"this is a {self.brand}")
        print(f"Model: {self.model} with a 4 wheel drive and {self.seats} seats")

car = Car("Toyota", 2018, 6)
car.car_details()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, post, salary):
        super().__init__(name, age)
        self.post = post
        self.salary = salary

    def show_details(self):
        print(f" My Name is {self.name}, I am {self.age} years old")
        print(f" I work as a {self.post}, Earning a net of {self.salary} in dollars per month")

    def tax_payble(self):
        tax = self.salary * (9.5/100)
        return tax

worker = Employee("Azeez", 28, "Backend Dev",50000)
Tax = worker.tax_payble()
worker.show_details()
print(f"My monthly income tax is: {Tax}")



# run this code by runing in thyour terminal ==> python 22_oop.py