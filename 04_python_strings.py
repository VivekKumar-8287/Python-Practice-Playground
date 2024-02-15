# Strings

a = 'Hello'
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
'''

# Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

# Square brackets can be used to access elements of the string.

print(a[1])

# Since strings are arrays, we can loop through the characters in a string, with a for loop.

for x in "banana":
    print(x)

# String Length
len()

# Check String
txt = "The best things in life are free!"
print("free" in txt)

# Check if NOT
txt = "The best things in life are free!"
print("expensive" not in txt)

# Slicing
b = "Hello, World!"
print(b[2:5])

# Slice From the Start
print(b[:5])

# Slice To the End
print(b[2:])

# Negative Indexing
print(b[-5:-2])

# Upper Case
print(a.upper())

# Lower Case
print(a.lower())

# Remove Whitespace
print(a.strip())

# Replace String
print(a.replace('H','J'))

# Split String
print(a.split(','))

# String Concatenation
c = a + b
print(c)

c = a + " " + b
print(c)

# String Format
# As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:

# But we can combine strings and numbers by using the format() method!

# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# Escape Character
# To insert characters that are illegal in a string, use an escape character.

# An escape character is a backslash \ followed by the character you want to insert.
""" 
\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
\ooo	Octal value	
\xhh	Hex value
 """

# String Methods
# Note: All string methods return new values. They do not change the original string.

