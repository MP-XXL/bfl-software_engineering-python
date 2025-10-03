def add1(func):
  def myinner(num):
    return func(num) +1
  return myinner

@add1
def myfunction(num):
  return num


print(myfunction(10))


