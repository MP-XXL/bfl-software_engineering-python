allowance = 2000.
print("We are buying books for 400")
books = 400
allowance -= books
print(allowance)

print("Found 100 bucks under the bed")
income = 100
allowance += income
print(allowance)

print("Bought snacks worth 250 quid")
snacks = 250
allowance -= snacks
print(allowance)

print("Gave 25% of current balance or allowance to your sibling")
percent = (25 / 100) * allowance
allowance -= percent
print(allowance)

print("Uses one-third of allowance to buy data")
data = (1 / 3) * allowance
allowance -= data
print(allowance)

print("Splits the balance equally between savings and tithes")
savingsNtithes = 2
allowance //= savingsNtithes
print(allowance)

print("Compare allowance by 100 and print what is left")
comparator = 100
allowance %= comparator
print(allowance)
