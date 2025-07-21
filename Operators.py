# ARITHMETIC OPERATOR
a = 15
b = 4

## Addition
print("Addition:", a+b)

## Subtraction
print("Subtraction:", a-b)

## Multiplication
print("Mutliplication:", a*b)

## Division
print("Divide:", a/b)

## Floor Division
print("Floor Division:", a//b)

## Modulus
print("Modulus:", a%b)

## Exponentiation
print("Exponentiation:", a**b)

# COMPARISON OPERATOR (==, >, <, !=, >=, <=)
a = 13
b = 42
print(a==b)
print(a<b)
print(a>b)
print(a!=b)
print(a>=b)
print(a<=b)

# LOGICAL OPERATOR (AND, OR, NOT)
a = True
b = False
print(a and b)
print(a or b)
print(not a)

# ASSIGNMENT OPERATOR
a = 8
b = 13
b += a
b <<= a
print(b)
print(b)
b -= a
print(b)
b *= a
print(b)
b /= a
print(b)
b //= a
print(b)
b %= a
print(b)
b **= a
print(b)


# IDENTITY OPERATOR (IS , IS NOT)
x = [1,2]
y = [1,2]
z = x
print(z is x) ## Same object
print(x is y) ## Same value but different object
print(x is not y)

# MEMBERSHIP OPERATOR (IN, NOT IN)
x = 20
y = 24
data = [12, 15, 18, 22, 24, 27, 29]

if x not in data:
    print("x is not present in the given list.")
else:
    print("x is present in the given list.")

if y in data:
    print("y is present in the given list.")
else:
    print("y is not present in the given list")

# BITWISE OPERATOR (&, |, ^, ~, <<, >>)
a = 5
b = 3

## Bitwise AND (&)
print(a&b)

## Bitwise OR (|)
print(a|b)

## Bitwise XOR (^)
print(a^b)

## Bitwise NOT(~)
print(~a)

## Left Shift(<<)
print(a<<b)

## Right Shift(>>)
print(a>>b)

# TERNARY OPERATOR
age = 18
status = "Adult" if age >= 18 else "Minor"
print(status)