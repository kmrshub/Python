# Print(Output) Function
print ("Hello World")

# Input Function
name = input("Enter your name: ")
print ("Hello,", name, "! Welcome!")

val = input ("Enter your value : ")
print (val) #By default the type of the returned object always will be String

name = input ("What is your name?\n")
print(name)

#Typecasting input into Integer
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
print("Sum is: ", num1 + num2)

#Typecasting input into Float
num3 = float(input("Enter First Number: "))
num4 = float(input("Enter Second Number: "))
print("Sum is: ", num3 + num4)

# Get a List as Input from User
user_input = input("Enter elements separated by Space: ").split()
print("List: ", user_input)

# Get a List as Input using Loop
a = []
n = int(input("Enter number of elements: "))
for i in range(n): #Appending elements to the list
    elements = input(f"Enter element {i+1}: ")
    a.append(elements)

print("List:", a)

# Get a list as input using map(). This is used when numeric inputs are needed (to convert them into integer)
user_input = list(map(int,input("Enter numbers separated by space: ").split()))
print ("List: ", user_input)

# Using List comprehension for concise Input (this is similar to loop)
n = int(input("Enter the number of elements: ")) #Get the number of elements
a = [input(f"Enter element {i+1}: ") for i in range(n)]
print ("List: ", a)

#Accepting a nested list input
user_input = [x.split(",") for x in input("Enter nested list: ").split(";")]
print("Nested List: ", user_input)

#Taking multiple inputs from users (2 inputs)
x,y = input("Enter two values: ").split()
print("Number of Boys: ", x)
print("Number of Girls: ", y)

#Taking multiple inputs from users (3 inputs)
x,y,z = input("Enter three values: ").split()
print("Total no of students: ", x)
print("Number of Boys: ", y)
print("Number of Girls: ", z)

#Taking conditional input from users in Python
age_input = input("Enter your age: ")
age = int(age_input)
if age <0:
    print("Please enter your valid age.")
elif age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen")

#Finding datatype of Input in Python
a = "Sonny Hayes"
b = 22
c = 11.56
d = ("Sonny", "Hayes", "JP", "Expensify")
e = ["Lewis", "Hamiliton", "MaxV", "LeClerek"]
f = {"Lewis": 6, "MaxV": 4}
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))

#####Scope of Variable
#     1. Local Variable
def my_function():
    x = 10
    print(x)
my_function()

#    2. Global Variable
x = 10
print(x)

#    3. Enclosing Variable (NonLocal)
def outer():
    y = 10
    def inner():
        nonlocal y
        y += 1
        print(y)
    inner()
    print(y)
outer()

#   4. Bulit-In Scope
print(len("Hello"))

#Shadowing Variable
x = 243

def function():
    global x
    x = 279
    print(x)
function()
print(x)
