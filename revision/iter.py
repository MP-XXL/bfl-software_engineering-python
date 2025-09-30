"""class Number:

    def __iter__(self):
        self.x = 1
        return self

    def __next__(self):
        y = self.x
        if self.x <= 5:
            self.x += 1
        else:
            raise StopIteration
        return y


my_number = Number()
a = iter(my_number)
print(next(a, "Max iteration Level error!"))
print(next(a, "Max iteration Level error!"))
print(next(a, "Max iteration Level error!"))
print(next(a, "Max iteration Level error!"))
print(next(a, "Max iteration Level error!"))
print(next(a, "Max iteration Level error!"))
"""

class CountDown:

    def __init__(self, stop=5, start=0, direction="down"):
        self.stop = stop
        self.direction = direction
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        x = self.start
        if self.direction == "up":
            if self.start <= self.stop:
                self.start +=1
            else:
                raise StopIteration
        elif self.direction == "down":
            if self.start >= self.stop:
                self.start -=1
            else:
                raise StopIteration
        else:
            return "Invalid direction!"

        return x
count = CountDown(stop = 1, start = 5, direction ="hi")
z = iter(count)
print(next(z, "Max countdown error!"))
print(next(z, "Max countdown error!"))
print(next(z, "Max countdown error!"))
print(next(z, "Max countdown error!"))
print(next(z, "Max countdown error!"))
print(next(z, "Max countdown error!"))
print(next(z, "Max countdown error!"))

