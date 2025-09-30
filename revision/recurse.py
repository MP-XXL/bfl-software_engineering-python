# Using recursion
# Shred date to be a single integer

def year_shreder(year):
    ult = []
    for cha in year:
        num = cha
        ult.append(int(num))
    print(ult)
    summ = 0
    for ele in ult:
        summ += ele
    print(summ)
    if summ > 9:
        year_shreder(str(summ))
    else:
        return summ
inxx = input("Enter birth date : ")
year_shreder(inxx)

