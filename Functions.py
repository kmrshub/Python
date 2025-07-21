#Defining a function
def test():
    print("This is a function.")

test()

#Function with Parameters
def greet(name):
    print("Hello, " + name + "!") # + symbol can be only used in the case of string
    print("Hello",name,"!") # can be used with any data type
greet("Sonny")

#Function with Return Value
## Example 1
def add(a,b):
    """Add two numbers and return the result""" #This is Docstring
    return a + b
result = add(3,5)
print(result)
help(add)
print(add.__doc__)

## Example 2
def addition(a,b):
    return a + b
sum1 = addition(4,7)
sum2 = addition(6,9)
total = sum1 + sum2
print(total)

#Function with Default Parameter
def greet(name = "Guest"):
    print("Hello, " + name + "!")
greet()
greet("Shubham") #Overwritting the default

#Function with Keyword Argument
def display(name, age):
    print(f"Name : {name}, Age: {age}")
display(age = 25, name = "Shubham")
display(25, "shubham") # This will give output but here we have used positional argument rather than keyword argument

#Special Symbol used for passing an argument in a Function of Python
## Non-Keyword Arguments (*)
### Example 1
def myfun(*args):
    for a in args:
        print(a)
myfun("Hello", "my","name", "is", "Shubham")
myfun("Hello my name is Shubham")

### Example 2 Combining multiple text
def join_words(*words):
    return " ".join(words)
welcome = join_words("Hello", "Shubham", "welcome")
print(welcome)

### Example 3 - Calculate the total sales for multiple regions
def total_sales(*sales):
    sum_total = 0
    for amount in sales:
        sum_total += amount
    return(sum_total)
result = total_sales(10000, 23460, 34212)
print("Total Sales: ", result)
# By using return statement the value can be stored in a variable which can be used later on as well

### Same example as above but with print statement
def last_sale(*sales):
    final_total = 0
    for amount in sales:
        final_total += amount
    print("Total Sales :", final_total)
last_sale(10000, 20000, 30000)
#By using print statement the value will not be stored.

### Example 4 : Messages Log
def log_msg(*message):
    for msg in message:
        print("Log: "+ msg)
log_msg('User LoggedIn', 'File Downloaded', 'Report Generated')

### Example 5 : Operator Function
def calculate(operator, *value):
    if operator == "add":
        return sum(value)
    elif operator == "multiply":
         result = 1
         for num in value:
             result *= num
         return result
    elif operator == 'average':
        if len(value) == 0:
            return 0
        return sum(value) / len(value)
    else:
        return "Unknown Operator"
print(calculate("add", 34, 2,56,23))
print(calculate("multiply", 5,7,2,8))
print(calculate('average', 20, 40, 60, 80))

##Keyword Argument (**kwargs)
### Example 1
def myFun(**details):
    for key, value in details.items():
        print(f"{key} = {value}")
myFun(name = "Shubham", gender = "Male", age = "30")

#Below example is same as above but instead of writting Key and Value we have used k and v
def myFun(**details):
    for k, v in details.items():
        print(f"{k} = {v}")
myFun(name = "Shubham", gender = "Male", age = "30")

# Functions within Functions
## Example 1
def f1():
    s = "Hello World!"

    def f2 ():
        print(s)
    f2()
f1()

## Example 2
def outer_function(name):
    def inner_function():
        print(f"Hello, {name}")
    inner_function()
outer_function("World")

## Example 3 : Returning the inner function
def outer():
    def inner():
        print("This is inner function")
    return inner
func = outer()
func()

## Example 4 : Finding n power of a number
def power(n):
    def number(x):
        return x ** n
    return number

square = power(2)
print(square(10))

### Example 5
def process_data(data):
    def clean(item):
        return item.strip().lower()
    return [clean(d) for d in data]
print(process_data(["Apple", "BaNaNa", "ORANGE"]))

# Anonymous Functions in Python (Lambda)
### Example 1
square = lambda x: x * x
print(square(5))

### Example 2
s1 = "Hello World!"
s2 = lambda func: func.upper()
print(s2(s1))

### Example 3 Adding two numbers
add = lambda a,b : a+b
print(add(4,8))

### Example 4 Lambda with if else statement (conditional)
n = lambda x: 'Positive' if x > 0 else 'Negative' if x < 0 else "Zero"
print(n(-4))
print(n(4))
print(n(0))

### Example 5 Lambda with multiple statement
calc = lambda x, y: (x+y, x*y)
res = calc(4,7)
print(res)

# Recursive Function
### Example 1
def factorial(n):
    if n == 0:
       return 1
    else:
        return n * factorial(n-1)
print(factorial(6))

