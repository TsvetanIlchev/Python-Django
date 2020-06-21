# Inheritance
class Animal():

    def __init__(self):
        print("Animal created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")

class Dog(Animal):

    def __init__(self):
        #The next line is not needed actually
        #Animal.__init__(self)
        print("Dog created")

    def bark(self):
        print("Woof")

    def eat(self):
        print("Dog eating")

animal = Animal()
animal.whoAmI()
animal.eat()

dog = Dog()
dog.whoAmI()
dog.eat()
dog.bark()
