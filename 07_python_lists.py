# List

# Lists are used to store multiple items in a single variable.

# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

# Lists are created using square brackets:

thislist = ["apple", "banana", "cherry"]

# List Items
# List items are ordered, changeable, and allow duplicate values

# List Length
print(len(thislist))

# type()
# From Python's perspective, lists are defined as objects with the data type 'list':
# <class 'list'>

# The list() Constructor
# thislist = list(("apple", "banana", "cherry")) # note the double round-brackets

# Python Collections (Arrays)
""" 
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
 """

# Access Items
print(thislist[1])

print(thislist[-1])

# Range of Indexes
print(thislist[2:5])

# Check if Item Exists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

# Change Item Value
thislist[1] = "blackcurrant"

# Change a Range of Item Values
thislist[1:3] = ["blackcurrant", "watermelon"]
# Change the second value by replacing it with two new values:
thislist[1:2] = ["blackcurrant", "watermelon"]
# Change the second and third value by replacing it with one value
thislist[1:3] = ["watermelon"]

# Insert Items
thislist.insert(2, "watermelon")

# Append Items
# To add an item to the end of the list, use the append() method:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")

# Insert Items
thislist.insert(1, "orange")

# Extend List
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)

# Add Any Iterable
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)

# Remove Specified Item
thislist.remove("banana")

# Remove Specified Index
# The pop() method removes the specified index.
thislist.pop(1)

# The del keyword also removes the specified index:
del thislist[0]

# The del keyword can also delete the list completely.
del thislist

# Clear the List
thislist.clear()

# Loop Through a List
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

# Loop Through the Index Numbers
# Use the range() and len() functions to create a suitable iterable.
for i in range(len(thislist)):
  print(thislist[i])

# Using a While Loop
  thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

# Looping Using List Comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

# List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

# The Syntax

# newlist = [expression for item in iterable if condition == True]

# Sort List Alphanumerically
thislist.sort()

# Sort Descending
thislist.sort(reverse = True)

# Customize Sort Function

# Reverse Order
thislist.reverse()

# Copy a List
mylist = thislist.copy()

# Another way to make a copy is to use the built-in method list().
mylist = list(thislist)

# Join Two Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

list1.extend(list2)

# List Methods
""" 
append()
clear()
copy()
count()
extend()
index()
insert()
pop()
remove()
reverse()
sort()
 """


