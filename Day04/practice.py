something = "a boy sleeps"
print(something.capitalize())

extra = "i just code and sleep"
print(extra.capitalize())

sleep = "sleep eludes me"
print(sleep.capitalize())

print(sleep[:1].upper() + sleep[1:])

decentralize = "everything should be decentralized!"
print(decentralize[0:1].upper() + decentralize[1:])

party = "party at disco"
dragon = "Eragon's"
new = party[0:8].capitalize()+ " " + dragon
print(new)


mail = "cuttingedage@bullocks.com"
domain = "gmail.com"
end = mail[-3:]
print(mail[:13] + domain + end)

varr = "cage"
length_of_varr = len(varr) // 2
first_half = varr[:length_of_varr]
print(first_half)

second_half = varr[length_of_varr:]
print(second_half)

xters = "pump"
word_length = len(xters) // 2
first_side = xters[:word_length]
print(first_side)

second_side = xters[word_length:]
print(second_side)

word = "cake"
word_length = len(word) // 2
first = word[:word_length]
print(first)

second = word[word_length:]
print(second)
