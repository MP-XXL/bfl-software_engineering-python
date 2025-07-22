# Task 1
'''
Create
1. A list of your your favourite movies
2. A list of numbers from 1 to 10
3. A mixed list with name, age, isMarried, gender, height and favourite colour
4. A list of your provisions
'''
favourite_movies = ["One Punch Man", "Kimetsu No Yaba", "Sakamoto Days", "Fire Force", "Smallville"]
print(favourite_movies)
numbers =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)
mixed_list = ["MP", 100, False, "male", 6.1, "black" ]
print(mixed_list)
provisions = ["milk", "sugar", "potatoes"]
print(provisions)

android = ["Samsung", "Techno", "Itel", "Redmi", "Oppo"]
ios = ["11_Pro-max", "15_Pro", "XR", "16 plus", "7_Plus"]
phones = [android, ios]
print(phones)

# Task 2
'''
Your are a secret agent , use the code letters below to decode the following words:
    1. Print "Hello"
    2. Print "World"
    3. Print the list in a reverse order
    '''
code = ["x", "H", "e", "z", "l", "l", "!", "p", "o", "-", "n", " ", "W", "@", "r", "d", "o", "#"]
print(code[1] + code[2] + code[4] + code[4] + code[8])
print(code[-6] + code[-2] + code[-4] + code[4] + code[-3])
print(code[::-1])

# Task 3
grid = [["The", "sky", "is"],["full", "of", "stars"], ["shining", "bright", "tonight"]]
'''
1. Print "The sky" using nested indexing.
2. Create a sentence: "The stars are shining" by picking and combining items from the grid and manually adding "are".
3. Reverse the second row of the grid print it.'''
print(grid[0][0] + " " + grid[0][1])
print(grid[0][0] + " " + grid[1][2] + " " + "are" + " " + grid[2][0] )
print(grid[1][::-1])


# Task 4

playlist = ["Song A", "Song B", "Song C"]

playlist[1] = "Song D"
print("Playlist after replacing 'Song A'", playlist)
playlist.append("Song E")
print("Playlist after adding 'Song E'", playlist)
playlist.insert(0, "Intro")
print("Final playlist :", playlist)


# Task 5
'''
Your are helping your teacher arrange students in a classroom. The clasroom starts empty. Follow the instructions to build the 
arrangement
1. Start with an empty list called desk.
2. Ask the user to enter the names of three students, one by one, and place them in the list
3. A student sitting in the second seat wants to be replaced. Ask for the new name and replace the old one
4. Another student walks in and wants to sit between the first and second students. Add them to the correct position.
5. Print the final list showing how the desks are arranged'''
desk = []

desk.append(input("Enter first student name : "))
desk.append(input("Enter second student name : "))
desk.append(input("Enter third  student name : "))

new_student = input("Enter new student name to replace student 2 : ")
desk[1] = new_student
walked_in_student = input("Enter name of student that walked in: ")
desk.insert(1, walked_in_student)
print("Final desk: ", desk)




