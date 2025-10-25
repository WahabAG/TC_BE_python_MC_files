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

"""Using the super() key word"""
# example

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Animals Makes sounds")


class Dog(Animal):

    def __init__(self, name, breed):
        super().__init__(name) # accessing the parent class
        self.breed = breed  # adding new method to child class
        self.color = "white black stripes"

    def sound(self):
        print(f"{self.name} barks!!")

    def height(self):
        return "3 meters"
    
    def color(self, color):
        self.color = color
        print(f"{self.name} barks!!")

dog = Dog("Trex", "Husky")
dog.sound()
print(dog.height())









# run this code by runing in thyour terminal ==> python 22_oop.py