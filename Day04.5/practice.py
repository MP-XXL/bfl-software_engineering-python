print("\n        **\n       *  *\n      *    *\n     *      *\n    *        *\n   *          *\n  *            *\n *              *")
print("******      ******")
print("     *      *")
print("     *      *")
print("     ********")
print("\n        **\n       *  *\n      *    *\n     *      *\n    *        *\n   *          *\n  *            *\n *              *")
print("******      ******")
print("     *      *")
print("     *      *")
print("     ********")

random_number = 384947372920
print(f"Rounded to 3 d.p {random_number:.3f}")

result = 5/2
print(result)
print(f"result rounded to 2 d.p = {result:.2f} ")

money = "3540040"
money = float(money)
print(f"Money properly separated = ${money:,.2f}")

sentence = "We are testing location of a word"
print("a" in sentence)
print("location" in sentence)
print("tary" in sentence)
print("tes" in sentence)
print("tion" in sentence)

print("Name|\tAge|")
print("MP|\t100")


print(sentence.startswith("we"))
print(sentence.startswith("We"))
print(sentence.endswith("word"))
print(sentence.endswith("Word"))

graduated = input("").lower()
print(graduated.startswith("true"))

failing = input("").upper()
print(failing.startswith("FALSE"))


flavours = "Vanilla, Red_Velvet, Chocolate, Strawberry"
print(flavours)
flavours = flavours.split(",")
print(flavours)

colours = "Red Blue Green Yellow Black Orange"
print(colours)
colours = colours.split(" ")
print(colours)
print(colours[4])


data = "cate Jos 300000.0 JS01"
data = data.split(" ")
print(data)
print("DATA SLIP")
print("----------------------")
print("Name:\t{}\nState:\t{}\nSalary:\t${:,.2f}\nID:\t{}".format(data[0].capitalize(), data[1], float(data[2]), data[3]))

print(" ")
groceries = "Carrots 20.0 Milk 30 eggs 15.0 honey 13.9994"
print(groceries)
groceries = groceries.split(" ")
print(groceries)
print("RECEIPT")
print("------------")
print("{}\t----\t${:.2f}\n{}\t----\t${:.2f}\n{}\t----\t${:.2f}\n{}\t----\t${:.2f}".format(groceries[0], float(groceries[1]), groceries[2], float(groceries[3]), groceries[4].capitalize(), float(groceries[5]), groceries[6].capitalize(), float(groceries[7])))
print("Total = ", float(groceries[1]) + float(groceries[3]) + float(groceries[5]) + float(groceries[7]))

print(" ")

moss = "GhostNet#X44CR#98.654#TRC8821"
print(moss)
print("TOP SECRET")
print("----------------")
print("Code Name:\t", moss[:5])
print("Message Code:\t", moss[8:14])
print("Message Class:\t", moss[8:9])
print("Trace ID:\t", moss[-7:-2])
print("Traceable:\tNO")
print("Severity Level:\t", moss[-14:-13])
