# a = "Hello, World!"

# file = open("world.txt", "w")
# file.write(a)


file = open("sample.txt", "r")

content = file.read()
print(content)

file.close()