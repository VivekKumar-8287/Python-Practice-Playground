# Tuple
# A tuple is a collection which is ordered and unchangeable.
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Tuple Items
# Tuple items are ordered, unchangeable, and allow duplicate values.

# type()
# <class 'tuple'>

# The tuple() Constructor
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets

# Access Tuple Items
thistuple[1]

# Negative Indexing
thistuple[-1]

# Range of Indexes
thistuple[2:5]

# Change Tuple Values
# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# Add Items
# 1. Convert into a list:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

# Add tuple to a tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

# Remove Items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

# Delete tuple
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

# Unpacking a Tuple

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

# Using Asterisk*
# If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

(green, yellow, *red) = fruits

(green, *tropic, red) = fruits

# Loop Through a Tuple

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

# Loop Through the Index Numbers
for i in range(len(thistuple)):
    print(thistuple[i])

# Using a While Loop
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

# Join Two Tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2

# Multiply Tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

# Tuple Methods
'''
count()
index()
'''

