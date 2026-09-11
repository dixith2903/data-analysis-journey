fruits = {"apple", "banana", "cherry", "date", "grape"}
print(fruits)

fruits.add("kiwi") # adds "kiwi" to the set
print(fruits)

fruits.update(["lemon", "mango"]) # adds multiple items to the set
print(fruits)

fruits.remove("banana") # removes "banana" from the set, raises KeyError if not found
print(fruits)

fruits.discard("dates") # removes "dates" from the set, does nothing if not found
print(fruits)

a = fruits.pop() # removes and returns an arbitrary element from the set
print(a)

fruits.clear() # removes all elements from the set
print(len(fruits)) # prints the number of elements in the set, which should be 0 after clear
print(fruits)