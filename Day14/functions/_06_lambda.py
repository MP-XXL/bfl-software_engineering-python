#learn mapping, filter,reduce in python
# Lambdas are functions without names, (annonymous function)
# Lambda functions return the result of their expression. They do not use return keyword

bio = lambda name: print(f"Hello {name}")
#print(bio("Tom"))
bio("Tom")


#print(lambda x, y: x + y,(2,2))
#lambda x, y: x + y
#print(2, 2)


#mapping example
exams_score = [30, 40, 50, 45, 10, 60]

results = map(lambda exam_score: exam_score + 10, exams_score)
print(list(results))
