def show_value():
    x = 10 # Local variable 'x' is defined within the function 'show_value'
    print(x)

show_value()
x = 20 # Global variable 'x' is defined outside the function

show_value() # This will print 10, as the local variable 'x' is used within the function
