names = ["Tommy", "Tony", "Ruby", "Sweety", "Scooby"]

print(names)
print(names[3])
print(type(names)) 
print(type(names[0]))

elements = [1, 2, 3, 4, 5, True, False]
print(elements)
print(len(elements))
print(elements[5])
print(elements[3:5])

# Lists in python are mutable, which means we can change their content after they have been created.

elements[0] = 10
print(elements)