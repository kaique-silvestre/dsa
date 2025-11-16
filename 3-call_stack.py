# I created this code just so i can debug it to see how the call stack really works

def first_function():
    print("Inside the first function")
    second_function()

def second_function():
    print("Inside the second function")
    third_function()

def third_function():
    print("We are inside the third function")


first_function()
