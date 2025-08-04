name = "Tanko"
if name == "Tanko":
    name = "Godiya"
    print(name)
print(name)

# Python gives an exception for if and while blocks for scoping. It is able to access inner variables. Hence Print equaled "Godiya, Godiya" and "Pumba, Pumba"
name = "Karly"
if name == "Karly":
    x = "Pumba"
    print(x)
print(x)

# Else Block
num = 10

if num > 10:
    print("Inside if block")
else:
    print("Hit else block!")
    if num == 10:
        print("Yes")

# Elif Block

num = 10

if num > 10:
    print("Inside if block")
elif num < 10:
    print("Inside elif block")
else:
    print("Hit else block!")
    if num == 10:
        print("Yes")

