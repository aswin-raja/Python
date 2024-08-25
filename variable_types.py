
# A variable is created the moment you first assign a value to it.
x = 5
y = "John"
print(x)
print(y)

#--------------------------------------------------------------------------------------------------------------------------------

# Variables do not need to be declared with any particular type, and can even change type after they have been set.
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#------------------------------------------------------------------------------------------------------------------------------

# Casting
# If you want to specify the data type of a variable, this can be done with casting.
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# Get the Type
# You can get the data type of a variable with the type() function.
x = 5
y = "John"
print(type(x))
print(type(y))

# Single or Double Quotes?
# String variables can be declared either by using single or double quotes:
x = "John"
# is the same as
x = 'John'

# Case-Sensitive
# Variable names are case-sensitive.
a = 4
A = "Sally"
#A will not overwrite a


# repr() function is used to obtain a string representation of an object
var = 9
print(type(repr(var)))


#------------------------------------------------------------------------------------------------------------------------------

# Legal variable names:

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#------------------------------------------------------------------------------------------------------------------------------

# Illegal variable names:

# 2myvar = "John"
# my-var = "John"
# my var = "John"

#------------------------------------------------------------------------------------------------------------------------------

# Many Values to Multiple Variables

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One Value to Multiple Variables

x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a Collection

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)


# create a variable outside of a function, and use it inside the function

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()


# Create a variable inside a function, with the same name as the global variable

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


# If you use the global keyword, the variable belongs to the global scope:

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

# To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


# Quiz link  https://realpython.com/quizzes/python-variables/viewer/
