##LOOPS
#Python has 2 primitive loop commands :
# while loop & for loop 

#THE WHILE LOOP  while loop we can execute a set of statements as long as a condition is true.
#i = 1
#while i < 6:
#    print(i)
#    i += 1 # 1 2 3 4 5 
#NOTE : we need to increment i or else code will go in loop 

#BREAK STATMENT 
#This statment we can stop the loop even if the while condyion is true 
#EXAMPLE :
#i = 1
#while i < 6:
#    print (i) 1,2 ,3
#    if i == 3:
#        break 
#    i += 1

#CONTINUE STATMENT
# This statement we can stop the current iteration and continue with the next one :
#EXAMPLE :
#i = 0
#while i < 6:
#    i += 1
#    if i == 3:
#        continue
#   print(i) 1 ,2,3,4,5,6

# Else Statment
# this statment we can run a block of code once when the condition no longer is true :
#EXAMPLE 
#m = 1
#while m < 6:
#    print(m) 1,2,3,4,5
#    m += 1
#else :
#    print("m is no longer less then 6") m is no longer less then 6

##FOR LOOP 
#FOR LOOP is used for iterating over a sequence (list , tuple , dictionary , set or a string)
#Example :
#fruits = ["apple","banana","kiwi"]
#for x in fruits:
#    print(x) apple , banana , kiwi

#The for loop does not require an indexing variable to set beforehand.

#LOOPING THROUGH STRING 
#Example:
#for x in "banana" :
#    print(x) b a n a n a

#Break and Continue statments 
# Break will stop the loop 
# Continue will stop one iterationa and start other iteration
#Example break :
#fruits = ["apple","banana","cherry"]
#for x in fruits:
#    print(x) apple , banana
#    if x == "banana":
#        break

#Example continue 
#fruits = ["apple","banana","cherry"]
#for x in fruits:
#    print(x) 
#    if x == "banana":
#        continue
#    print(x) apple apple , banana , banana, cherry , cherry

#range() function
# it loop a set of code for specific number of time 
#EXAMPLE 
#for x in range(8):
#   print(8) 888888888

#for x in range(0,9):
#    print(x) 0 1 2 3 4 5 6 7 8

#for x in range (8 , 60 , 2):
#    print(x)  8 10 12 14 16 ..... 58

#ELSE
#else keyword is used it execute the code when loop is completed
#Example 
#for x in range(6):
#   print(x) 0 1 2 3 4 5
#else:
#    print("Finally completed") Finally completed

#break and else 
#Example 
#for x in range(3):
#    if x == 2: break 
#    print(x) 0 1 
#else:
#    print("Done")

#NESTED LOOP 
#in this loop is inside loop 
#Example 
#a = ["apple","banana","kiwi"]
#b = ["red","yellow","green"]
#for x in b:
#    for y in a:
#        print(x,y) red apple , red banana, red kiwi,...,green banana,green kiwi

#pass statment
# this statment is used when there is no content is there to put in loop 
#Example 
#for x in [0,1,2]:
#    pass 
#no output but runs the code 