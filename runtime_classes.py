
class Animal:
    def move(self):
        print("moving...")

class Dog(Animal):
    def bark(self):
        print("Woof!")

d = Dog()
d.bark()
d.move()

CLASS_NAME = "cat"
myclass = type(CLASS_NAME, (Animal,), {'meow': lambda self: print("MEOW MEOW")})

c = myclass()
c.move()
c.meow()