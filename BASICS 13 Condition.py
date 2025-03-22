#If..Else#
#Python Conditions 
# It supports logical conditions frpm math:
#Equals : a==b
#Not Equals: a != b
#Less than: a < b
#Less than or equal to : a <= b
#Greater than : a > b
#Greater than or equal to: a >= b

#If Statements
#a = 23
#b = 200
#if b > a:
#    print("b is greater than a") "b is greater than a "

#INDENTATION
#Instead of curel brackets .. Whitespace at the beginning of a lines are used has a indentation in python.
#If statement, without indentation (will raise an error)
#a = 23
#b = 200
#if b > a:
#print("b is greater than a") #Indentation Error

#Elif = "if the previous conditions were not true, then try this condition".
#a = 4
#b = 25
#if b > a:
#    print("b is greater than a") 
#elif a == b : 
#    print("a and b are equal to each other") b is greater than a

#Else = its like it gives final condtion at the end 
#a = 200
#b = 250
#if b > a:
#    print("b is greater than a")
#elif a == b:
#    print("a is equal to b")
#else :
#    print ("a is greater than b") b is greater than a
#a = 200
#b = 25
#if b > a:
#    print("b is greater than a")
#else :
#    print ("a is greater than b")a is greater than b

#SHORT HAND IF = If you have only one statement to execute, you can put it on the same line as the if statement.
#a=10
#b=2
#if a > b : print("a is greater") a is greater

#SHORT HAND IF .. ELSE = one statement to execute, one for if, and one for else, you can put it all on the same line:
#a = 330
#b = 330
#print ("A") if a > b else print ("B")  B a = 2 ; b = 330
#print ("A") if a > b else print ("=") if a == b else print ("B") =

#AND = is keyword is a logical operator, and is used to combine conditional statements

#a = 200
#b = 33
#c = 500
#if a > b and c > a:
#    print ("Both Condtions are True") "Both Condtions are True

#OR
#a = 200
#b = 33
#c = 500
#if a > b or a > c : print("Atleast one condtion is true")Atleast one condtion is true"

#NOT
#a = 33
#b = 200
#if not a>b: print("b is greater")b is greater

#Nested If = if statements inside if statements, this is called nested if statements
#x = 41 
#if x > 10:
# print("Above ten")
# if x > 20:
#  print ("and also above 20!")
#else:
# print ("but not above 20.") Above  , and also above 20!

#PASS STATMENT = if statment cannot be kept empty o in that case pass is used if there is not print statment is there 
#a= 33
#b = 200
#if b > a:
#   pass 
