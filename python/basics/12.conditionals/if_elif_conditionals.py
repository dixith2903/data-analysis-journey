marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Fail")

if marks % 2 == 0:
    print("The marks are even.")
else:
    print("The marks are odd.")