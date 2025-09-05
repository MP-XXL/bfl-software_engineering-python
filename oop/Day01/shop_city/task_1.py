# Create and instantiate classes

class Animals:

    def __init__(self, name, ani_class, legs):
        self.name = name
        self.ani_class = ani_class
        self.legs = legs


animal = Animals("Dog","Mammal", 4)
print(animal.name)



class Cars:


    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color


car = Cars("Volkswagen", "Jetta", "Red")
print(car.color)


class Students:

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height


student1 = Students("Lolo", 12, 75)
print(student1.age)


class House:

    def __init__(self, color, design):
        self.color = color
        self.design = design


house1 = House("Brown", "Cottage")
print(house1.design)


class Footwear:

    def __init__(self, brand, color, size):
        self.brand = brand
        self.color = color
        self.size = size


shoes = Footwear("Nike", "White", 43)
print(shoes.brand)
