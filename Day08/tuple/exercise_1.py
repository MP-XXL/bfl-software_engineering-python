response = (4,)
print(type(response))

response = (True, "Welcome", ["email", "username"])
#print(type(response))
print(response[2])
print(response[2][1])
a = 1,
print(type(a))
print(type(response))
print(type(list(response)))

# or


response = list(response)
print(type(response))
response[0] = False
print(type(response), response)

a = (1, 2, 3)
b = (4, 5, 6)
x = b + a
print(x)

success, message, data = response
print(success)
print(message)
print(data)

