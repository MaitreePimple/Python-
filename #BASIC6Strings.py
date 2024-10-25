#Python Strings
#STRINGS
#print("HELLO") HELLO
#print('HELLO') HELLO

#QUOTES INSIDE QUOTES
#print("It's alright") It's alright
#print("His name is 'RAM'") His name is 'RAM'
#print("He is called 'SHAM'") He is called 'SHAM'

#ASSIGN STRING TO A VARIABLE

#a="MAITREE"
#print(a) MAITREE

#MULTILINE STRINGS
#a = """Lorem ipsum dolor sit amet,
#consectetur adipiscing elit,
#sed do eiusmod tempor incididunt
#ut labore et dolore magna aliqua."""
#print(a) //Lorem ipsum dolor sit amet,
#consectetur adipiscing elit,
#sed do eiusmod tempor incididunt
#ut labore et dolore magna aliqua.//

#a = '''Lorem ipsum dolor sit amet,
#consectetur adipiscing elit,
#sed do eiusmod tempor incididunt
#ut labore et dolore magna aliqua.'''
#print(a)
#Lorem ipsum dolor sit amet,
#consectetur adipiscing elit,
#sed do eiusmod tempor incididunt
#ut labore et dolore magna aliqua.

# Strings are Arrays  strings in Python are arrays of bytes representing unicode characters.
#Square brackets can be used to access elements of the string.
#a="Hello , world!"
#print(a[1]) e

#STRING LENGTH
#a = "HELLO,WORLD!"
#print(len(a)) 12

#CHECK STRING To check if a certain phrase or character is present in a string, we can use the keyword in.
#txt = "The best things in life are free!"
#print("free" in txt) True 

#Use it in an if statement:
#txt = "The best thing in life is free!"
#if "free" in txt :
#    print("Yes,'Free' is present.") Yes,'Free' is present.

#CHECK IF NOT phrases not present
#txt = "The best thing in life are free!"
#print("expensive" not in txt) True

#txt = "The best things in life are free!"
#if "expensive" not in txt:
#    print("No,'expensive' is not prsent") No,'expensive' is not prsent

#SLICING STRINGS
#b="Hello, Python!"
#print(b[2:5]) llo
#print(b[:5]) Hello
#print(b[5:]) , Python!
#print(b[-5:-2]) thon 

#MODIFY STRINGS
#a= "Hello, My world!"
#print(a.upper()) HELLO, MY WORLD!
#print(a.lower()) hello, my world!
#print(a.strip()) Hello, My world! remove whitespace
#print(a.replace("H","J")) Jello, My World!
#print(a.split(",")) ['Hello','My world!']

#STRING CONCATENATION 
#a = "Hello"
#b ="World"
#c = a + b
#print(c) HelloWorld
#c = a + " " + b
#print(c) Hello World

#FORMAT STRINGS
#F-STRINGS 
#age = 36
#txt = f"My name is Maitree, I am {age}"
#print(txt)  My name is Maitree, I am 36
#Placeholders and Modifiers
#A placeholder can contain variables, operations, functions, and modifiers to format the value.
#price = 59
#txt=f"The price is {price} dollars"
#print(txt) The price is 59 dollars
#txt = f"The price is {price:.2f} dollars"
#print(txt) The price is 59.00 dollars
#txt = f"The price is {20*59} dollars"
#print(txt) The price is 1180 dollars

#ESCAPE CHARACTERS
#txt = 'It\'s alright.'
#print(txt) It's alright
#txt = "This will insert one \\ (backslash)."
#print(txt) This will insert one\(backslash)
#txt = "Hello\nWorld!"
#print(txt) Hello
 #          world!
#txt1 = "Hello\rWorld!"
#print(txt1) World!
#txt2 = "Hello\tWorld!"
#print(txt2)Hello  World!
 #This example erases one character (backspace):
#txt3 = "Hello \bWorld!"
#print(txt3) HelloWorld!
#A backslash followed by three integers will result in a octal value:
#txt4 = "\110\145\154\154\157"
#print(txt4)Hello
 #A backslash followed by an 'x' and a hex number represents a hex value:
#txt5 = "\x48\x65\x6c\x6c\x6f"
#print(txt5) Hello
#STRING METHODS
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning