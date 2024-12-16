#LIST used to store multiple items in a single variable.
#mylist =["apple","banana","cherry"]
#print(mylist)

#LIST ITEMS 
#List items are ordered, changeable, and allow duplicate values.
#List items are indexed, the first item has index [0], the second item has index [1] etc.

#ORDERED
#it means that the items have a defined order, and that order will not change.
#If you add new items to a list, the new items will be placed at the end of the list.
#some can 

#CHANGEABLE
#meaning that we can change, add, and remove items in a list after it has been created.

#ALLOW DUPLICATES
#mylist=["apple","banana","cherry","apple","cherry"]
#print(mylist)  "apple","banana","cherry","apple","cherry"

#LISTLENGTH
#print(len(mylist)) 5

#List Items - Data Types
#list1 = ["apple", "banana", "cherry"]
#list2 = [1, 5, 7, 9, 3]
#list3 = [True, False, False]
#print (list1,list2,list3)
#print(type(list1)) <class 'list'> type()
#thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
#print(thislist)['apple','banana','cherry'] #the list() constructor

#Python Collections (Arrays)
#There are four collection data types in the Python programming language:

#List is a collection which is ordered and changeable. Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#Dictionary is a collection which is ordered** and changeable. No duplicate members.
#Set items are unchangeable, but you can remove and/or add items whenever you like.
#As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

#Access List Items
#List items are indexed and you can access them by referring to the index number
#mylist=["apple","banana","cherry"]
#print(mylist[1]) banana
#print(mylist[-0])apple
#print(mylist[0:3]) "apple","banana","cherry"
#print(mylist[:3]) "apple","banana","cherry"
#print(mylist[0:]) "apple","banana","cherry"
#print(mylist[-0:-3])[]

#mylist=["apple","banana","cherry"]
#if "apple" in mylist:
 #   print("Yes, 'apple' is in the fruits list") Yes, 'apple' is in the fruits list

#CHANGE LIST ITEMS 
#mylist = ["apple","banana","cherry"]
#mylist[1] = "blackcurrant"
#print(mylist) 'apple","blackcurrant","cherry'
#mylist[1:3] = ["blackcurrant", "watermelon"]
#print(mylist) apple, blackcurrant", "watermelon
#mylist[1:2] = ["blackcurrant", "watermelon"]
#print(mylist)  apple, blackcurrant", "watermelon ,cherry
#mylist.insert(2, "watermelon")
#print(mylist)apple banana watermelon cherry
#mylist = ['apple', 'banana', 'cherry']
#mylist[1:2] = ['kiwi', 'mango']
#print(mylist[2])

#ADD LIST ITEMS
#APPEND
#thislist = ["apple", "banana", "cherry"]
#thislist.append("orange")
#print(thislist) ppple banana cherry orange 
#INSERT
#mylist = ["apple","banana","cherry"]
#mylist.insert(1,"orange")
#print(mylist) apple orange banana cherry 
#EXTEND
#mylist =["apple","banana","cherry"]
#tropical = ["mango","pineapple","papaya"]
#mylist.extend(tropical) apple","banana","cherry "mango","pineapple","papaya
#print(mylist)
#ADD ANY ITERABLE
#mylist = ["apple","banana","cherry"]
#mytuple=("kiwi","orange")
#mylist.extend(mytuple)
#print(mylist)  "apple","banana","cherry", "kiwi","orange

#REMOVE LIST ITEMS 
#Remove Specified Item
#thislist = ["apple", "banana", "cherry"]
#thislist.remove("banana")
#print(thislist)
#thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
#thislist.remove("banana")
#print(thislist)
#thislist = ["apple" , "banana", "cherry"]
#thislist.pop(1)
#print(thislist)
#thislist = ["apple", "banana", "cherry"]
#del thislist[0]
#print(thislist)
#thislist = ["apple", "banana", "cherry"]
#del thislist
#print(thislist) (this cause error)
#thislist = ["apple", "banana", "cherry"]
#thislist.clear()
#print(thislist)
#LOOP LISTS
#FOR LOOP
#thislist = ["apple", "banana", "cherry"]
#for x in thislist:
  #print(x)
#Loop Through the Index Numbers
#thislist = ["apple", "banana", "cherry"]
#for i in range(len(thislist)):
  #print(thislist[i])

#WHILE LOOP
#thislist = ["apple","banana","cherry"]
#i = 0
#while i < len(thislist):
#  print(thislist[i])
#  i = i + 1

# Looping Using List Comprehension
#thislist = ["apple", "banana", "cherry"]
#[print(x) for x in thislist] [None,None,None]

#List Comprehension (OFFERS A SHORTER SYNTAX WHEN YOU WANT TO CREATE A NEW LIST BASED ON ORGINALLY CREATED LIST)

#fruits = ["apple" , "banana", "cherry" , "kiwi" , "mango"]
#newlist = [] (tHIS WILL PRINT NEWLIST WHICH CONTAINTS A IN THERE LETTER)
#for x in fruits:
  #if "a" in x :
   # newlist.append(x)
#print(newlist) 

#fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
#newlist = [x for x in fruits if "a" in x]
#print(newlist) (same code bt in short form)

#SYNTAX 
#newlist =[expression for item in iterable if condition == True]

#condition  (its like a filter that only accepts the item that valuate to True)
#example
#fruits = ["apple" , "banana" , "cherry","kiwi"]
#newlist = [x for x in fruits if x!="apple"]
#print(newlist) (OUTPUT "banana" , "cherry","kiwi")

#newlist = [x for x in fruits]
#print(newlist) (output ["apple" , "banana" , "cherry","kiwi"])

#Iterable (reapted objects)
#newlist = [x for x in range(10)]
#print(newlist) (Output[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

#with conditions
#newlist = [x for x in range(10) if x < 5]
#print(newlist) (output [0,1,2,3,4])

#EXPRESSION (it gives a list item in the new list)

#fruits = ["apple" , "mango" , "banana" , "kiwi" , "cherry"]
#newlist = [x.upper()for x in fruits] (makes every letter in uppercase)
#print(newlist) [APPLE , MANGO , BANANA , KIWI , CHERRY]

#newlist = ['hello' for x in fruits]
#print(newlist) ['hello','hello',...]

#newlist = [x if x !="banana" else "orange" for x in fruits]
#print(newlist) ["apple" , "mango" , "orange" , "kiwi" , "cherry"]

### SORT LIST ###
#Sort List Alphanumerical /ascending 
#thislist = ["orange","mango","kiwi","pineapple","banana"]
#thislist.sort()
#print(thislist) (output ['banana', 'kiwi', 'mango', 'orange', 'pineapple'])

#thislist = [100, 50,65,82,23]
#thislist.sort()
#print(thislist) [23,50,65,82,100]

#sort descending (everything is same just use reverse = True)
#thislist = ["orange" , "mango" , "kiwi" , "pineapple","banana"]
#thislist.sort(reverse=True)
#print(thislist) ['pineapple', 'orange', 'mango', 'kiwi', 'banana']
#thislist = [100, 50,65,82,23]
#thislist.sort(reverse = True)
#print(thislist) (output [100, 82, 65, 50, 23])

#Customize Sort Function
#def myfunc(n):
 # return abs(n - 50)
#thislist = [100,50,200,23,25,45]
#thislist.sort(key=myfunc) (it will sort by how the number is close to 50)
#print(thislist)[50, 45, 25, 23, 100, 200]

#Case Insensitive Sort (sort is case sesitive it will sort all the captial letter then lower letter in list)
#thislist = ["banana" , "Oranage" , "Kiwi" , "cherry"]
#thislist.sort()
#print(thislist)[Kiwi,Oranage ,banana , cherry]
#for insensitive sorting we have to command it "str.lower"

#RESVERSE ORDER
#thislist = ["banana" , "Orange" , "Kiwi" , "cherry"]
#thislist.reverse()
#print(thislist) ['cherry', 'Kiwi', 'Orange', 'banana']

###Copy Lists###

#thislist = ["apple","banana","kiwi"]
#mylist = thislist.copy()
#print(mylist) (output['apple','banana''kiwi])

#thislist = ["apple","banana","cherry"]
#mylist = list(thislist)
#print(mylist) ['apple','banana','cherry']

#Slice Operator
#thislist = ["apple","banana","cherry"]
#mylist = thislist[:]
#print(mylist) (output ['apple', 'banana', 'cherry'])

###JOIN LIST###
#list1 =["a","b","c"]
#list2 = [1,2,3]
#list3 = list1 + list2
#print(list3)['a','b','c',1,2,3]
#using append
#for x in list2:
 #   list1.append(x)
#print(list1)(output['a','b','c',1,2,3])
#using extand
#list1.extend(list2)
#print(list1) (output['a','b','c',1,2,3])

