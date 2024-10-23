#MANY VALUES TO MULTIPLE VARIABLES
#x,y,z = "orange","Banana","Cherry"
#print(x) #orange
#print(y)#Banana
#print(z) #Cherry

#ONE VALUE TO MULTIPLE VARIABLES
#x=y=z="orange"
#print(x)#orange
#print(y)#orange
#print(z)#orange

#Unpack a Collection (from given tuple , it allows to extract values)
#fruits = ["apple","banana","cherry"]
#x,y,z = fruits
#print(x) #apple
#print(y) #banana
#print(z) #cherry

#OUTPUT VARIABLES
#x = "Python is awesome"
#print(x) Python is awesome

#x = "Python"
#y = "is"
#z = "awesome"
#print(x,y,z) Python is awesome
#print(x+y+z) Pythonisawesome

#x = 5
#y = 10
#print(x+y) 15
#z = "Maitree"
#print(x+z) "Err will come 2 differnt data types they are + wont work"
#print(x,z) 5 Maitree

#Global Variables
#x = "awesome"
#def myfunc():
 #   print("Python is " + x) #Python is awesome
#myfunc()

#x = "awesome"
#def myfunc():
 #   x = "amazing"
  #  print("Python is "+ x) Python is amazing
#myfunc()
#print("Python is "+ x) Python is awesome

#THE GLOBAL KEYWORD
#def myfunc():
 #   global x
#    x = "AMAZING"
#myfunc()
#print("Python is "+ x) Python is AMAZING

#x = "amazing"
#def myfunc():
 #   global x 
  #  x = "lovely"
#myfunc()
#print("Python is " + x) Python is lovely