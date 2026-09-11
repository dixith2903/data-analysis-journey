Student = {
    "name": "Deekshith",
    "age": 20,
    "course": "B.Tech",
    "university": "XYZ University",
    "city": "Bangalore"
}
# Using pop() method to remove and return the value of the 'course' key

Student.pop("university")  # This will remove the 'university' key and its value from the dictionary
print(Student)

# Using popitem() method to remove and return the last key-value pair added to the dictionary
Student["CGPA"] = 8.5  # Adding a new key-value pair to the dictionary
print(Student)

Student.popitem()  # This will remove the last key-value pair added, which is 'CGPA': 8.5
print(Student)

# keys() method to get a view of all the keys in the dictionary
print(Student.keys())

# values() method to get a view of all the values in the dictionary
print(Student.values())

# items() method to get a view of all the key-value pairs in the dictionary
print(Student.items())

# Using clear() method to remove all items from the dictionary
Student.clear()  # This will remove all key-value pairs from the dictionary, leaving it empty
print(Student)