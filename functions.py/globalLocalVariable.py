# Global And Local Variable

# local variable - A variable that is defined inside a function and can only be accessed within that function.
 def greet():
    name = "sapna" #local variable
    print("hello",name)
greet()    

def greet():
    msg = "Hello!"
    print("Inside function:", msg) #inside function: Hello!

greet()
print("Outside function:", msg) # this will give an error because msg is a local variable and cannot be accessed outside the function.

# Global variable - A variable that is defined outside of any function and can be accessed from anywhere in the code.
name ="Rahul" #global variable
def greet():
    print("hello",name)
greet() # this will give the output because name is a global variable and can be accessed inside the function.