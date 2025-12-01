colors = list()
colors.append('red')
print(colors[0])
print()

x = 5  # x = 
print(type(colors), type(x))

t = type(colors)

new_thing = t()
new_thing.append('wombat')
print(new_thing)

class Dog:
    def bark(self):
        print("Woof! woof!")

d1 = Dog()
d2 = Dog()
print(type(d1), type(d2))
d1.bark()
d2.bark()


