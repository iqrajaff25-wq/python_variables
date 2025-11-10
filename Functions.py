#ChatGPT said:

# Types of functions:

# Built-in Functions
# User-defined Functions
# Lambda (Anonymous) Functions
# Recursive Functions
# Higher-order Functions
# Generator Functions
# Nested Functions
# Decorator Functions

# 01_Built-in Functions
# These are pre-defined in Python
    # print()     # Displays output
    # append()    # Add elements in list
    # remove()    # Remove an element from list
    # len()       # Returns length of a sequence
    # type()      # Returns the type of an object
    # range()     # Generates a sequence of numbers
    # sum()       # Returns the sum of all items in an iterable
    # max()
    # min()
    # sorted()

# 02_User-defined Functions
# Functions that you create using the def keyword.
def sum():
    num1 = int(input('Enter first number: '))
    num2 = int(input("Enter second number: "))
    total= num1 + num2
    print(f"The Sum of {num1} & {num2} is {total}")

# can be called like:
sum()

# i.e.:
def subtract(num1,num2):
    num1 = int(input('Enter first number: '))
    num2 = int(input("Enter second number: "))
    result = num1 - num2
    print(f"By Substracting {num2} from {num1}, we get {result} ")
subtract(2 , 1 )


# 03_Lambda (Anonymous) Functions
#These are one-line, nameless functions created with the lambda keyword.
#Oftenly used for short & simple tasks.

#i.e:
square = lambda x: x**2
print(square(5))   # Output: 25

#i.e:
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums))
print(squared)


# 04: Recursive Functions
#A function that calls itself to solve a smaller instance of the same problem.

#i.e.:
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))   # Output: 120

#factorial(5)
# = 5 * factorial(4)
# = 5 * (4 * factorial(3))
# = 5 * (4 * (3 * factorial(2)))
# = 5 * (4 * (3 * (2 * factorial(1))))


#05 Nested Functions
# Functions defined inside other functions (useful for encapsulation). 

def outer():
    def inner():
        print("Inside inner function")
    inner()

outer()


# i.e.:

def subtract(num1,num2):
    def multiply(num1,num2):
        multi = num1 * num2
        print(f"By Multiplying {num1} to {num2}, we get {multi}")
    multiply(10, 20)   
    subt = num2 - num1
    print(f"{num2} - {num1} = {subt}")
subtract( 20 , 22 )






