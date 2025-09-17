quote = input("What is your favourite quote? : ")
file_name = input("Where do you wish to store this 'quote'? : ")
with open(file_name, "w") as file:
    file.write(quote)
test = open(file_name, "r")





