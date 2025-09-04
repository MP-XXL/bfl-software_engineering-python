class Person:
    pass


p = Person()
print(p)

class Animal:
    pass
dog = Animal()
print(dog)

class Person:
    def say_hi(self):
        print("Hello, how are you?")


p = Person()
p.say_hi()
Person().say_hi()

class Animal:

    def identify_ani(self):
        print("I am ", dog)


dog = Animal()
dog.identify_ani()

class Person:
    def __init__(self, name):
        self.name = name


    def say_hi(self):
        print("Hello, my name is", self.name)

    
p = Person("Swaroop")
p.say_hi()

class Animal:

    def __init__(self, name):
        self.name = name

    def identify_ani(self):
        print("Hello, I am ", self.name)

g = Animal("Goat")
g.identify_ani()
Animal("Goat").identify_ani()
