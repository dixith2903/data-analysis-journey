age = "20"
print(type(age))  # This will print <class 'str'>, indicating that age is a string
# print(age + 9)  # This will concatenate the string "20" with the int 9, resulting in error
print(int(age)+9)  # This will convert the string "20" to an integer and then add 9, resulting in 29

price = "19.99"
print(type(price))  # This will print <class 'str'>, indicating that price is a string
print(float(price)+5)  # This will convert the string "19.99" to a float and then add 5, resulting in 24.99


a = 10
print(str(a))  # This will convert the integer 10 to a string "10"

num = "9087d"
# print(int(num))  # This will raise a ValueError because "9087d" cannot be converted to an integer

