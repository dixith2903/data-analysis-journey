Student_1 = {
    "name": "Deekshith",
    "age": 20,
    "course": "B.Tech",
    "university": "XYZ University",
    "city": "Bangalore"
}

Student_2 = {
    "name": "Deeksha",
    "age": 22,
    "course": "B.Sc",
    "university": "ABC University",
    "city": "Mumbai"
}

print(Student_1)

print(Student_2["name"])
print(Student_1["age"])

# print(Student_1["dob"])  # This will raise a KeyError since 'dob' is not a key in the dictionary

print(Student_1.get("dob"))  # This will return 'Key not found' instead of raising an error

Student_1["city"] = "Mangalore"  # Updating the value of the 'city' key in Student_1
print(Student_1)