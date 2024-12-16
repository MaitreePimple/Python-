##TUPLE##
# used to store multipke items in a single varable  # Tuple "()" constructor 
#Tuple is collection which is ordered and unchangeable #
#Tuple items are ordered , unchangeable and allow duplicate values and it starts from 0th index
#Order will not be changed 
#Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
#Allow Duplicate means apple can be added twice in same tuple 
##EXAMPLE :
#thistuple = ("apple","kiwi","strawberry","banana","apple")
#print(thistuple) # ("apple","kiwi","strawberry","banana","apply")

#TUPLE LENGTH ## to find tuple length 
#thistuple = ("apple","kiwi","strawberry","banana","apple")
#print(len(thistuple)) #5

##TUPLE WITH ONE ITEM##
#thistuple=("apple",)
#print(type(thistuple)) #<class 'tuple'>
#thistuple=("apple")
#print(type(thistuple)) #<class 'str'>

##ACCESS TUPLE ITEM##
#thistuple = ("apple","mango","banana","strawberry")
#print(thistuple[1]) #mango
#thistuple = ("apple","mango","banana","strawberry")
#print(thistuple[-1])#strawberry (negative index)
#RANGE
#thistuple = ("apple","mango","banana","strawberry","apple","mango","banana","strawberry")
#print(thistuple[2:5])#("banana","strawberry","apple") it return values withthen that range 
#thistuple = ("apple","mango","banana","strawberry","apple","mango","banana","strawberry")
#print(thistuple[0:])("print fromstart to end item in tuple")
#thistuple = ("apple","mango","banana","strawberry","apple","mango","banana","strawberry")
#print(thistuple[:8]) #"apple","mango","banana","strawberry","apple","mango","banana","strawberry")
#thistuple = ("apple","mango","banana","strawberry","apple","mango","banana","strawberry")
#print(thistuple[-4:-1]) (apple,mango,banana)
#thistuple = ("apple","banana","cherry") (Check if items exits)
#if "apple" in thistuple:
#    print("Yes ,apple is in the fruits tuple ") Yes ,apple is in the fruits tuple

##Update Tuples##
#Tuples are unchangebale or immutable but we can do like this tuple to list and then we can change list and then again convert to tuple 
#example 
#x = ("apple","mango","banana")
#y = list(x)
#y[2] = "kiwi"
#x = tuple(y)
#print(x) (apple,mango,kiwi)
#To add item in tuple we can follow the same steps 
#x = ("a","b","c")
#y = list(x)
#y.append("d")
#x = tuple(y)
#print(x) (a,b,c,d)
#x = ("mango","apple")
#y = ("apple",)
#x += y
#print(x) (mango,apple,apple)
#For REMOVING itemms from Tuple same steps to follow just remove the not required item 
#thistuple = ("apple","banana","pineapple","strawberry")
#y = list(thistuple)
#y.remove("apple")
#thistuple = tuple(y)
#print(thistuple) ("banana","pineapple","strawberry")
#thistuple = ("apple","banana","cherry")
#del thistuple #del keyword is used here
#print(thistuple) (error is displayed since tuple is completly deleted )

##UNPACKING TUPLE##
# Tuple values assigned are know has packing tuple and we can unpack them unpack means  allowed to extract the values back into variables
#example
#fruits =("apple","mango","pineapple")
#(green , yellow , red) = fruits
#print(green) apple
#print(yellow) mango
#print(red) pineapple
# using '*' asterisk
#fruits = ("apple", "mango","pineapple")
#(green , blue , *pink) = fruits
#print(green) apple
#print(blue) mango
#print(pink)['pineapple']
#(green , *tropic , pink) = fruits
#print(green) apple
#print(tropic) ['mango']
#print(pink) pineapple

##LOOP TUPLE##
# for loop and while loop 
# with help of for loop you can do by index number too
#thistuple = ("apple","banana","pineapple")
#for x in thistuple:
#    print(x) (it printed the items in vertical way like list)
#thistuple=("mango","banana","strawberry")
#for i in range(len(thistuple)): (used keywords like range and len)
#    print(thistuple[i]) (it listed down the items)
#thistuple = ("apple","mango","pineapple")
#i = 0
#while i < len(thistuple):
#    print(thistuple[i]) (it listed down the items)
#    i=i+1

##JOIN TUPLE##
# Join Two Tuples using'+'
#tuple1=("apple","mango")
#tuple2=("banana","apple")
#tuple3 = tuple1+tuple2
#print(tuple3) (apple, mango,banana,apple)

#Multiply Tuple ('*')
#tuple1 =("a","b")
#tuple2 = tuple1* 2
#print(tuple2) (a,b,a,b)

##TUPLE METHODS ##
#count() = number of value occured in the given tuple 
#index() = Searches the tuple for a specified value and returns the position of where it was found
