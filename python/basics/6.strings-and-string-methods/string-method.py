name = "Deekshith  "

print(len(name)) # This will print the length of the string "Deekshith" which is 9.
print(name.lower()) # This will print the string in lowercase: "deekshith"
print(name.upper()) # This will print the string in uppercase: "DEEKSHITH"
print(name.strip()) # This will remove any leading and trailing whitespace from the string: "Deekshith"
print(len(name.strip())) # This will print the length of the stripped string, which is 9.

print(name.replace("Deekshith", "Dixith")) # This will replace "Deekshith" with "Dixith": "Dixith"

print(name.isalpha()) # This will check if all characters in the string are alphabetic. It will return False because of the spaces.
print(name.isnumeric()) # This will check if all characters in the string are numeric. It will return False because of the letters and spaces.

