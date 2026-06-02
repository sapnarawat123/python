# Pass Functions- pass is a keyword in python that is used when we want to define a function but we don't want to implement its logic immediately
def greet():
    pass
greet() # this will not give any output because the function is not implemented yet.  

# In Conditional Statements
def evenOdd(nums):
    if(nums%2==0):
        pass # this will not give any output because the function is not implemented yet. We can use pass to avoid syntax error when we want to implement the logic later.
    else:
        return "odd"

print(evenOdd(5))
print(evenOdd(10)) 

# In Loops
for i in range(5):
    if(i==3):
        pass
    else:
        print(i)

# The pass statement in Python is a placeholder. It tells Python:
# "Do nothing for now, but don't give an error."
