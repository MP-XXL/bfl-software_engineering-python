#QUESTION 1

my_age = 100
pi = 3.14159
magic_number = ((my_age * 3) + pi) % 7
print(magic_number, "is the magic number and of type ", type(magic_number))


#QUESTION 2

secret_word = "PythonIsAmazing"
#Printing the first 6 characters of the string using slicing
print(secret_word[:6])

#Printing the first 6 characters of the string using indexing
print(secret_word[0])
print(secret_word[1])
print(secret_word[2])
print(secret_word[3])
print(secret_word[4])
print(secret_word[5])


#Printing the last 7 characters of the string using negative indexing
print(secret_word[-7])
print(secret_word[-6])
print(secret_word[-5])
print(secret_word[-4])
print(secret_word[-3])
print(secret_word[-2])
print(secret_word[-1])


#Printing the word "Is" using slicing
print(secret_word[6:8])

#Printing the string reversed using slicing
print(secret_word[::-1])

#Printing every second character in the string (using step slicing ::2).
print(secret_word[1::2])


#QUESTION 3
#Converting the first word "Python" to uppercase and printing it
print(secret_word[:6].upper())

#Converting "IsAmazing to lowercase and printing it"
print(secret_word[6:].lower())

#Combining both parts into one new string and printing it
first_half = secret_word[:6].upper()
second_half = secret_word[6:].lower()
new_string = first_half + second_half
print(new_string)

