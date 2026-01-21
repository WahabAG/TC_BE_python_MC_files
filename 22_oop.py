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
# class Vehicle:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

# class Car(Vehicle):
#     def __init__(self, brand, model, seats):
#         super().__init__(brand, model)
#         self.seats = seats

#     def car_details(self):
#         print(f"this is a {self.brand}")
#         print(f"Model: {self.model} with a 4 wheel drive and {self.seats} seats")

# car = Car("Toyota", 2018, 6)
# car.car_details()


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def race(self):
#         race = "caucassian"
#         return race

# class Employee(Person):
#     def __init__(self, name, age,  post, salary):
#         super().__init__(name, age)
#         self.post = post
#         self.salary = salary

#     def show_details(self):
#         print(f" My Name is {self.name}, I am {self.age} years old")
#         print(f" I work as a {self.post}, Earning a net of {self.salary} in dollars per month")

#     def tax_payble(self):
#         tax = self.salary * (9.5/100)
#         return tax

#     def race(self):         # polymorphisim of the race parent class
#         race = "black"
#         print(f"i am of african race which means i am {race}")

# worker = Employee("Azeez", 28, "Backend Dev",50000)
# Tax = worker.tax_payble()
# worker.show_details()
# print(f"My monthly income tax is: {Tax}")

# worker.race()  #polymorphysim calling

# class task
# practicing poly morphism
# class Calculation :
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2
    
#     def calculate(self):
#         pass

# class Adder(Calculation):

#     def __init__(self, num1, num2):
#         super().__init__(num1, num2)

#     def calculate(self):
#        return self.num1 + self.num2


# class Multiplier(Calculation):

#     def __init__(self, num1, num2):
#         super().__init__(num1, num2)

#     def calculate(self):
#        return self.num1 * self.num2
    

# multiplication = Multiplier(15, 3)
# mult_result = multiplication.calculate()
# print(mult_result)

# addition = Adder(15, 7)
# add_result = addition.calculate()
# print(add_result)


class Employee:
    specie = "Human"        # class attribute
    def __init__(self, name, sex, salary):
        self.name = name        # instance attribute
        self.sex = sex          # instance attribute
        self._salary = salary

    def get_salary(self):
        return self._salary

    def set_salary(self, salary):
        self._salary = salary



    def taxation(self):
        tax = self._salary * (14/100)
        print(tax)

    def apply_bonus(self):
        self._salary = ((25/100) * self._salary) + self._salary
        self._salary

staff = Employee("Azeez", "male", 200000)

print(Employee.specie)

staff.taxation()
print(staff.get_salary())
staff.set_salary(500000)

staff.taxation()
print(staff.get_salary())
# run this code by runinghtis in your terminal ==> python 22_oop.py

