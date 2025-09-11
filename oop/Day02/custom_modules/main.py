from mp import Mp

random_list = Mp()


random_list.append(8)
print(random_list)
random_list.append(2)
random_list.append(5)
random_list.append(7)
print(random_list)
random_list.remove(7)
print(random_list)
random_list.pop()
#random_list.pop(1)
print(random_list)
random_list.insert(1, "Tag")
print(random_list)
