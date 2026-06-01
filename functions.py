def fun():
     print("Welcome to GFG")

fun();

# Function Arguments

def evenOdd(num):
    if(num%2==0):
        return "even"
    else:
        return "odd"
print(evenOdd(10))
print(evenOdd(5))

# Types of Function Arguments
# 1.Default Arguments- used when no value is passed to the function, it takes the default value.

def greet(name="Guest"):
    print("Hello",name)

greet()

# 2. Keyword Arguments- used when we want to pass the value to the function by using the name of the parameter.
def greet(name,age):
    print("hello",name, "you are",age,"years old")

greet(age=27,name="Sapna")    

# 3 Positional Arguments- used when we want to pass the value to the function in the same order as the parameters are defined.
def greet(name,age):
    print("hello",name,"you are",age)

greet("sapna",27)
greet(27,"sapna") 
#  this will give wrong output because the order of the arguments is not correct.

# 4. Arbitrary Arguments- allow functions to accept multiple values. This is done using two special symbols:
#  a.1. *args — Multiple positional arguments - *args collects extra values into a tuple.
def greet(*args):
    for name in args:
        print("hello",name)
greet("sapna","sneha","priya")

# 2. **kwargs — Multiple keyword arguments

# **kwargs collects extra named values into a dictionary.
def greet(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")

greet(name="sapna",age=27,city="delhi")        