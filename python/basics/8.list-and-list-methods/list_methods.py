fruits = ["apple", "banana", "cherry"]
print(fruits)

# Append method adds an item to the end of the list
fruits.append("mango")
print(fruits)

# Insert method adds an item at a specified index
fruits.insert(1, "orange")
print(fruits)

# Extend method adds all items of an iterable (like another list) to the end of the list
more_fruits = ["grape", "kiwi"]
fruits.extend(more_fruits)
fruits.extend(["watermelon", "pineapple"])
print(fruits)

# Remove method removes the first occurrence of a specified value
fruits.remove("banana")
print(fruits)

# Pop method removes and returns the item at a specified index (default is the last item)
fruits.pop(2)  # Removes "cherry"
print(fruits)

# # Clear method removes all items from the list
# fruits.clear()
# print(fruits)

# Index method returns the index of the first occurrence of a specified value
print(fruits.index("mango"))

# Count method returns the number of occurrences of a specified value
print(fruits.count("apple"))

# Sort method sorts the list in ascending order (for strings, it sorts alphabetically)

numbers = [55, 23, 78, 12, 34, 69, 99]
numbers.sort()
print(numbers)

numbers.sort(reverse=True)  # Sort in descending order
print(numbers)