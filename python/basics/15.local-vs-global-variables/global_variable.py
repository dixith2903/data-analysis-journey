x = 69 # Global variable
def show_value():
    x =96 # Local variable
    print(x) 

show_value()
print(x)


y = 42 # Global variable
def display_value():
    global y # Declare 'y' as global to modify it within the function
    y = 24
    print(y)

display_value()
print(y)