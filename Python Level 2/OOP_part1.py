# class Sample():
#     pass
#
# x = Sample()
# print(type(x))

# class Dog():
#
#     # Class object attribute
#     species = "mammal"
#
#     def __init__(self, breed, name):
#         self.breed = breed
#         self.name = name
#
# mydog = Dog(breed = "Lab", name = "Lordy")
# otherdog = Dog(breed = "Huskie", name = "Sammy")
#
# print(mydog.breed)
# print(mydog.name)
# print(mydog.species)

class Circle():

    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return self.radius*self.radius * Circle.pi

    def set_radius(self, new_r):
        self.radius = new_r

mycircle = Circle(3)
# mycircle.radius = 100
mycircle.set_radius(999)
print(mycircle.radius)
print(mycircle.area())
