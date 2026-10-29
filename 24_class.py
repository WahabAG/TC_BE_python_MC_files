### revisiting class inheritance, polymorphism
## Example 1
class Animal:
    def __init__(self):
        print("Animal first appearace")

    def whatType(self):
        print(" I can either live on land or water..")

    def ability(self):
        print("I can either walk, swim or fly..")





class MyBird:
    family = "Aves"
    def __init__(self):
        print("My Bird first appearace")

    def whatType(self):
        print("i am a bird and i live in trees or land.")

    def ability(self):
        print("i can fly and sing..")


class Penguin(MyBird):
    def __init__(self):
        super().__init__()  #inheritace from parent class
        print("Penguin first appearace")

    def ability(self):  # overiding from parent class
        print("i can swim and walk..")

    def color(self):  # new class attribute
        print("i am black and white..")

class Parrot(MyBird):
    def __init__(self, name, color):
        super().__init__()  #inheritace from parent class
        self.name = name
        self.color = color
        print(f"Parrot first appearace, name: {self.name}, color: {self.color}")


bird = MyBird()
bird.whatType()
bird.ability()
print(f"{"_" * 5} \n" )

pg1 = Penguin()
pg1.color()
pg1.ability()
print(f"{"_" * 5} \n" )

pr1 = Parrot("Polly", "green")



## Example 2   Child class can inherit from multiple parent classes
class vertebre:
    def __init__(self):
        print("I am a vertebre animal..")
    def bones(self):
        print("I have well defined bone structure..")
    def feature(self):
        print("I have a backbone..")


class Fish(vertebre, Animal):
    def __init__(self):
        super().__init__()
        print("I am a fish..")
    def feature(self): #overriding the vertebre parent class method
        print("I have fins and gills..")
    def ability(self): #overriding the Animal parent class method
        print("I can swim..")
    def scale(self):
        print("I have pretty scales..")


salmon = Fish()
salmon.bones()
salmon.feature()
salmon.ability()
salmon.scale()



# INSTRUCTIONS FOR TESTING
# 1. Launch your terminal and run the code
# 2. Run the code -> python 24_class.py