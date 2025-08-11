import random

# NUMERIC (SCALAR) DATA TYPE
## Integer (int)
a = 10
print(type(a))

## Float
a = 10.0
print(type(a))

## Complex
a = 2 + 3j
print(type(a))
print(a.real)
print(a.imag)

# BOOLEAN DATA TYPE
## True and False
a = True
b = True
c = False
print(a+b+c, type(a))

# NONE TYPE (Represents absence of value)
a = None
print(type(a))

# TEXT TYPE
name = "Shubham"
print(type(name))
print(name[0]) # Strings are immutable and supports slicing
print(name[-1])

#SEQUENCE TYPE
## LIST - Ordered, heterogenous, mutable collection. It allows duplicate as well
### Syntax of List : my_list = [item1, item2, item3]
fruits = ['apple', 'banana', 'strawberry']
print(fruits)

### Accessing elements of list
print(fruits[0]) # Accessing elements of list by index
print(fruits[0:1]) # Accessing elements of list by slicing
print(fruits[1:])
print(type(fruits))

### Searching in List
#### Using in Operator
print('apple' in fruits)

#### Using index(value)
print(fruits.index('apple'))

#### Using count(value)
print(fruits.count('banana'))

### Modifying a List
#### Changing the existing value
fruits[2] = 'orange'
print(fruits)

#### Adding items to the list using .append()
fruits.append("strawberry") # This will create a new index(last) in the list fruits and add strawberry to that index.
print(fruits)

#### Adding items to the list using .insert()
#### Index function inserts the element in the given index position and shifts the existing element in the next index position, it does not overwrite the existing element
fruits.insert(1, 'kiwi')
print(fruits)
fruits.insert(10,'mango') # If the index is bigger than the list, it doesn't create gap, instead it inserts the element in the last.
print(fruits)
fruits.extend(['melon', 'pear'])
print(fruits)
fruits.insert(-1,'guava')
print(fruits)
fruits.append('banana')
print(fruits)

### Looping through List
#### Using for loop
for fruit in fruits:
    print(fruit)

#### Using enumerate() for index and value
for index, value in enumerate(fruits):
    print(index,value)

### Sorting and Reversing a List
#### Using sort() - Modifies original list
fruits.sort()
print(fruits)

#### Using sorted(list) - Returns new sorted list
sorted_fruits = sorted(fruits)
print(sorted_fruits)

#### Reversing a list using reverse()
fruits.reverse()
print(fruits)

### Copying a List
#### Using copy()
new_fruits = fruits.copy()
print(new_fruits)

#### Using slicing[]
brand_fruits = fruits[1:4]
print(brand_fruits)

#### Using list()
old_fruits = list(fruits)
print(old_fruits)

### Removing items from list
#### Removing items from List using remove()
fruits.remove('banana')
print(fruits)

#### Removing items from List using pop()
fruits.pop()  # This will remove last item from list
print(fruits)
fruits.pop(-1)  # This will remove items as per the index position
print(fruits)

#### Removing items from list using del
del fruits[0]
print(fruits)

#### Removing items from list using clear()
fruits.clear()
print(fruits)

### List function
print(len(new_fruits))
print(min(new_fruits))
print(max(new_fruits))
print(list(new_fruits))
p = 'Shubham'
print(list(p))

### Nested List
vegetables = ['potato', 'tomato', ['eggplant','pumpkin'], ['cauliflower', 'cabbage']]
print(vegetables[2])
print(vegetables[2][1])

## TUPLE - Ordered, immutable

### Ways to create a tuple
#### Normal
point = (10,20)
print(type(point))

#### Creating a tuple without parentheses
my_tuple = 10, 20, 30, 40, 50, 60
print(my_tuple, type(my_tuple))

#### Creating a tuple with single element
sample = (10,)
print(sample, type(sample))

### Accessing an element from Tuple
print(my_tuple[0])
print(my_tuple[-1])

### Slicing tuple
print(my_tuple[0:3])
print(my_tuple[2:])
print(my_tuple[:3])
print(my_tuple[::2])
'Syntax for above is [start:stop:step], start by default is 0, stop by default is last index and step by default is 1'
print(my_tuple[1::2])

### Unpacking a Tuple
t = (1,2,3)
a,b,c = t
print(a,b,c)

### Nested Tuple
new_tuple = (1,2,3,(4,5,6,7),8,9,10,(11,12,13))
print(new_tuple[3])
print(new_tuple[7][2])

## RANGE
r = range(5)
print(list(r), type(r))
print(r)

# SET TYPE
## Set - Unordered, unique and mutable
### Syntax
#### Normal way
nums = {1,2,3,4}
print(nums, type(nums))

#### Using set() constructor
my_set = set([1,2,3,4,5,6,7])
print(my_set)

sample_set = set()
print(sample_set)

### Duplicates are ignored in sets
xy = {1,1,1,2,3,4,5,5,6,7,8,8,9,9,10}
print(xy)

### Adding Elements to set
#### Using add()
my_set.add(11)
print(my_set)

#### Adding multiple elements using update()
my_set.update([8,9,10],(12,13,14))
print(my_set)
'Update expects a single iterable or mulitple iterable like sets, tuple, list and string'

string_set = {'apple', 'banana'}
string_set.update('kiwi')
print(string_set)

test_set = {1,2,3}
test_set.update("456")
print(test_set)

### Removing Elements from set
#### Using remove()
my_set.remove(10)
print(my_set)
'remove() will throw error if the element is not present in the set'

my_set.discard(11)
print(my_set)
'discard() does not throws error even when value is not present'

### SET Operations
s = {1,2,3,4,5,6,7}
t = {4,5,6,7,8,9,10}
#### Union - all items from both sides
print(s.union(t))

#### Intersection - Common items
print(s.intersection(t))

#### Difference - items in a not in b
print(s.difference(t))

#### Symmetric Difference - items in either but not in both
print(s.symmetric_difference(t))

### Removing Items from set
#### Using pop()
popped_item = s.pop()
print("Popped Item:", popped_item)
print("Set after pop:", s)

#### Using clear()
s.clear()
print("Set after clear: ", s)

## Frozenset - Immutable sets
x = frozenset([1,2,4,5])
print(x,type(x))

# MAPPPING TYPE
## DICTIONARY - key-value pairs
student = {"name":"Shubham", "age": 25, "city":"Patna"}
print(student, type(student))

# TYPE CASTING
a = int("10") # string to int
print(a,type(a))

b = float("3.5")
print(b,type(b))

c = str(100)
print(c,type(c))

# TYPE CHECKING
x = 5
print(type(x))
print(isinstance(x,int)) # This checks whether the taken object is of the instance specified

# RANDOM NUMBERS
z = random.randint(1,100)
y = random.random()
print(z)
print(y)
