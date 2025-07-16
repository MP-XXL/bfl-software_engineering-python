#TEXT

user1 = "Mark"
user2 = 'K9ine'
user3 = "MP"

#using constructor function

user4 = str("Molly")
user5 = str("Poppins")
user6 = str('Baggins')

userX = '''
        I am user X, and my name is Xian
        I live in Beijin
        I am a pythonista!
        '''

print(userX)

#strings are stored in python in an array format with every character having an index number.

print(userX[22])
print(user4[2])

company_name = "Blockfuse"

print(company_name[0])
print(company_name[1])
print(company_name[2])
print(company_name[3])
print(company_name[4])
print(company_name[5])
print(company_name[6])
print(company_name[7])
print(company_name[8])

#SLICE

print(company_name[2:5])

#slicing from the start value

print(company_name[:5])


#slicing from the end value

print(company_name[5:])

quote = "Five slice of bread"
chain = "blockchain"
number = 50
total = 1

print(quote[:4])
print(quote[5:10])
print(quote[11:13])
print(quote[14:])

print(number + len(chain) + total)

#Using  negavtive start and end points; the 0 index is not included. It sarts from -1

technology = "blockchain"

print(technology[-10:-1])

print(technology[-10:])

print(technology[-5:-1])


uppercase = technology.upper()
lowercase = technology.lower()
print(uppercase, lowercase)
print(technology.upper())
print(technology.lower())


bio = "Programmer"

one_half = bio[-7:]
other_half = bio[-10: -7]
upperGrammer = one_half.upper()
print(other_half.upper())
print(one_half.lower())
print(upperGrammer) 
