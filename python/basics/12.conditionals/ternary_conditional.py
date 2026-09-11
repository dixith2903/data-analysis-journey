age = int(input("Enter your age: "))

# Using ternary conditional operator to determine if the person is an adult or a minor
status = "Adult" if age >=18 else "Minor"

print(f"You are {status}.")