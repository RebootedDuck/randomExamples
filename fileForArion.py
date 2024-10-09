'''
range(0,100) returns an iterator which for loops through from 0,99 - where I is the current position on that loop, so this prints the numbers 0,99 - 100 is NOT printed which confused me when I first learned it
'''
for i in range(0,100):
    print(i)
    
list = ["cat", "dog", "mouse"] # Lists can hold anything, strings, ints, or more lists
print(list[0]) # list indexes start at 0 and are accessed with [] - This will return cat

for i in list: # This loops through every index of the list and i is whatever value it's currently at, this prints the entire list step by step
    print(i)
    
for idx, i in enumerate(list): # By using enumerate you can have the current index position and the actual value be accessible, useful if you need to know what iteration you're at
    print(i, idx)
    
def function(string: str): # This defines a function and defines it to have one argument which is a string, the "string" part defines the name of the variable inside the function, :str defines the input should be a string
    print(string)
    
list.append("chicken") # use .append to add to a list

print(list[-1]) # Accessing negative indexes reads backwards, this will return chicken