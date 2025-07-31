# Tuple
a = ("a")
print(type(a))
a = ("a",)
print(type(a))
a = ([True, False])
print(type(a))
a = ([True, False],)
print(type(a))

server_response = ("Active", True, 500, [600, ["Air"], 1.0])
print(server_response[1:4])
print(server_response[3][2])

server_response = list(server_response)
print(type(server_response))
server_response.append(False)
print(server_response)
status, online, *others = server_response
print(status)
print(online)
print("The rest of the tuple data: ", *others)
