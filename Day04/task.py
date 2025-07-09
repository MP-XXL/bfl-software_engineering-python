#Task 1
email = "user@domain.com"
attachment = "gmail"

first = email[:5]
end = email[-4:]
email = first + attachment + end
print(email)


#Task 2

word = "pythonista"
word_length = len(word) // 2
first_half = word[:word_length]
print(first_half)

second_half = word[word_length :]
print(second_half)
