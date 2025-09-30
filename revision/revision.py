# Prompt user for their favourite quote
quote = input("What is your favourite quote? : ")
"""file_name = input("Where do you wish to store this 'quote'? : ")"""
"""with open(file_name, "w") as file:
    if file_name.endswith(".txt"):
        file.write(quote)
    else:
        with open(file_name + ".txt", "w") as file:
            file.write(quote)
    with open(file_name, "r") as file:
        test = open(file_name, "r")"""
# Stop program from terminating when user does not enter the right file name extension
while True:
    file_name = input("Where do you wish to store this 'quote'? : ")
    if file_name.endswith(".txt"):
        with open(file_name, "w") as file:
            file.write(quote)
            print("file successfully saved!")
            with open(file_name, "r") as file:
                print(file.read())
            break # Terminate the loop when all the right conditions are met
    elif file_name.endswith(".pdf"):
        print("We do not support .pdf!")
    else:
        print("Please provide a '.txt' extension for your file name!")






