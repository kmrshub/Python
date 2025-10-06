# Magic or Dunder methods
print(dir(int))

#Creating an empty Class
class Car():
    pass

car1 = Car()
car2 = Car()

car1.speed = 200
car2.speed = 300

car1.company = 'Tata'
car2.company = 'Mahindra'

car1.color = 'Black'
car2.color = 'Red'

print("Car1 Details are -", "Model:", car1.company,",", "Color:", car1.color,",", "Speed:", car1.speed)
print("Car2 Details are -", "Model:", car2.company,",", "Color:", car2.color,",", "Speed:", car2.speed)

# Creating a class but with print statement inside it
class Bike():
    def show_details(self):
        print(f"Company: {self.company}, Model: {self.model}, Color: {self.color}")

bike1 = Bike()
bike2 = Bike()

bike1.company, bike1.model, bike1.color = 'Kawasaki', 'Duke 390', 'Black'
bike2.company, bike2.model, bike2.color = 'Royal Enfield', 'Hunter 350', 'White & Blue'

bike1.show_details()
bike2.show_details()

# Excercise 1 : Create an empty class Animal using pass, create two objects animal1 and animal2,
# assign attributes manually (animal1.name = "Dog", animal1.sound = "Bark", animal2.name = "Cat", animal2.sound = "Meow")
# and print their attributes.

class Animal:
    pass

animal1 = Animal()
animal2 = Animal()

animal1.name, animal2.name = 'Dog', 'Cat'
animal1.sound, animal2.sound = 'Barks', 'Meows'

print("First Animal is", animal1.name, "and it", animal1.sound)
print("Second Animal is", animal2.name, "and it", animal2.sound)


# Exercise 2 : Create a class Person with attributes name and age using __init__,
# add a method show_info() to print name and age, create two objects with different values and call show_info().

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Person's name is {self.name} and age is {self.age}")

person1 = Person("Shubham", 30)
person2 = Person("Kumar", 30)

person1.show_info()
person2.show_info()

# Exercise 3 : Create a class Calculator with methods add(a, b), subtract(a, b), multiply(a, b), and divide(a, b),
# then create an object and perform all operations.

class Calculator:
    def addition(self, a, b):
        return a+b

    def substraction(self, a, b):
        return a-b

    def multiply(self, a, b):
        return a*b

    def divide(self, a, b):
        if b!=0:
            return a/b
        else:
            return "Error! Division by zero"

calc = Calculator()

print("Addition:", calc.addition(10,13))
print("Substraction:", calc.substraction(23,14))
print("Multiplication:", calc.multiply(12,23))
print("Division:", calc.divide(200, 40))
print("Division", calc.divide(10,0))

# Exercise 4
# Create a class BankAccount with attributes owner and balance (default = 0), add methods deposit(amount),
# withdraw(amount), and show_balance(), then create two accounts and test them.

class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount # Here we are not using self.amount as its a temporary value passed to the method

    def withdrawal(self, amount):
        if self.balance!=0:
            self.balance -= amount
        else:
            print("Low balance, cannot withdraw")

    def show_balance(self):
        print(f"{self.owner}'s your account balance is {self.balance}")

customer1 = BankAccount("Avanish", 100000)
customer2 = BankAccount("Vishal")
customer3 = BankAccount("Kusharg")

customer1.deposit(10000)
customer2.deposit(100000)

customer1.withdrawal(20000)
customer2.withdrawal(15000)
customer3.withdrawal(1000)

customer1.show_balance()
customer2.show_balance()
customer3.show_balance()

# Exercise 5
# Create a class Car with attributes brand and speed (default = 0), add methods accelerate(value), brake(value),
# and show_speed(), then create a car object and test accelerate and brake.

class CAR:
    def __init__(self, brand, speed=0):
        self.brand = brand
        self.speed = speed

    def acceleration(self, value):
        self.speed += value

    def brake(self, value):
        if self.speed != 0:
            self.speed -= value
        else:
            print(f"{self.brand}'s car is already in stationary position.")

    def show_speed(self):
        if self.speed !=0:
            print(f"{self.brand}'s car speed is {self.speed}")
        else:
            print(f"{self.brand}'s car is stationary")

car1 = CAR("Toyota", 130)
car2 = CAR("Hyundai")
car3 = CAR("Mahindra")

car1.acceleration(40)
car2.acceleration(150)

car1.brake(30)
car2.brake(50)
car3.brake(20)

car1.show_speed()
car2.show_speed()
car3.show_speed()

# Exercise 6
# Create a class Student with attributes name and marks (list of marks), add methods add_mark(mark) and average(),
# then create a student, add some marks, and print average.

class Student:
    def __init__(self, name):
        self.name = name
        self.mark = []

    def add_marks(self, marks):
        """Add a marks to the student marks list"""
        self.mark.append(marks)

    def avg_marks(self):
        """Calculate and return average of all marks"""




