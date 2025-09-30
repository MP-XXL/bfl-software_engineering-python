import sys

print("Hello world!")

print(sys.version)

cage = [1,2,3,4,5]

w = r = t = "red"
print(w+r+t)
z = 5
print(f"{z}{t}")

def test_func():
    #global z
    #z += 1
    #c = z
    z = "Flow"
    print(z)
    #print(c)
z = 6
test_func()
print(z)

z = 1j

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
