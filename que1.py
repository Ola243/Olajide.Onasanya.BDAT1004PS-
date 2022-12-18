"""
Question 1
Consider the following Python module:
After importing the module into the interpreter, you execute:
>>> b()
>>> b()
>>> b()
>>> a
?
What value is displayed when the last expression (a) is evaluated? Explain your
answer by indicating what happens in every executed statement.
"""

a = 0


def b():
    global a
    a = c(a)


def c(a):
    return a + 2

b()
b()
b()
print(a)

"""
>>> b() # calling the function

def b():
    global a # using global to modify the global a variable
    a = c(a) # calling c() function with a as an parameter having value 0


def c(a): # a = 0
    return a + 2 # will return a + 2 means 0 + 2 = 2


# Then
>>> b() # calling the function 2nd time

def b():
    global a # using global to modify the global a variable
    a = c(a) # calling c() function with a as an parameter having value 2


def c(a): # a = 2
    return a + 2 # will return a + 2 means 2 + 2 = 4


# Then
>>> b() # calling the function 3rd time

def b():
    global a # using global to modify the global a variable
    a = c(a) # calling c() function with a as an parameter having value 4


def c(a): # a = 4
    return a + 2 # will return a + 2 means 4 + 2 = 6

a # this statement will print the value of global variable a
"""