##SETS##
#SETS ARE USED TO STORE MULTIPLE ITEMS IN A SINGLE VARIABLE 
#SET ITEMS ARE UNCHANGEABLE , UNORDERED AND DO NOT ALOOW DUPLICATE VALUES
#IN SET "{}" this constructor is used 
#EXAMPLE :
#thisset = {"apple","banana","cherry"}
#print(thisset) # {"apple","banana","cherry"}
#print(len(thisset)) #3 (set length)
#print(type(thisset)) <class 'set'> (data type of set)

## ACCESS ITEMS IN SET ##
#IN SET YOU CANNOT ACCESS ANY ITEM BUT YOU CAN ASK IF ANY SPECIFIC ITEM OR ELEMENT IS PRSENET IN SET BY USING FOR LOOP OR in KEYWORD
#thisset = {"hello" , "world"}
#for x in thisset :
#    print(x) #hello world printed in vertical form 
#print("world" in thisset) #True 

## ADD SET ITEMS ##
#IN SET YOU CANNOT CHANGE ITS ITEM BUT YOU CAN ADD NEW ITEM 
#add()method is used 
#thisset = {"HELLO" , "CODING" , "PYTHON"}
#thisset.add("PROG") 
#print(thisset) #{"HELLO" , "PROG" , "PYTHON" ,"CODING"}
#ADD SETS (update() method is used)
#thisset = {"apple", "banana", "cherry"}
#set2 = {"pineapple", "mango", "papaya"}
#thisset.update(set2)
#print(thisset)  {"apple", "banana", "cherry","pineapple", "mango", "papaya"}
#ADD ANY ITERABLE (tuples ,list and dictionaries etc)
#thisset ={"apple","kiwi"}
#thislist=["mango","Grapes"]
#thisset.update(thislist)
#print(thisset) {"apple","kiwi","mango","Grapes"}

## REMOVE ITEMS ##
#remove(),discard() ,pop (),clear(),del() methods are used in it 
#when using the pop() method, you do not know which item that gets removed.
#thisset = {"apple", "banana", "cherry"}
#thisset.remove("apple") it will raise error if item is not prsent in set
#print(thisset) {"cherry", "banana"}
#thisset.discard("apple") will not raise an error if the item is not prsent in the set
#print(thisset) {"cherry", "banana"}
#x=thisset.pop()
#print(x) banana
#print(thisset) {'apple','cherry'}
#thisset.clear() # it empties the set
#print(thisset) set()
#del thisset
#print(thisset) ERROR

##LOOP SETS ##
#ONLY FOR LOOP IS USED IN IT 
#thisset = {"apple","kiwi"}
#for x in thisset:
 #   print(x) kiwi , apple 

##JOIN SETS ##
#union() and update() methods joins all items from both sets.
#intersection() method keeps ONLY the duplicates.
#difference() method keeps the items from the first set that are not in the other set(s).
#symmetric_difference() method keeps all items EXCEPT the duplicates.

#UNION (|)
#set1 = {"a","b","c"}
#set2 = {1,2,3}
#set3 = set1.union(set2)
#print(set3) #{c,1,a,2,3,b}
#set3 = set1|set2
#print(set3) {1,b,a,2,3,c}

#JOIN MULTIPLE SETS 
#set1 = {"a", "b", "c"}
#set2 = {1, 2, 3}
#set3 = {"John", "Elena"}
#set4 = {"apple", "bananas", "cherry"}
#myset = set1.union(set2,set3,set4)
#print(myset) {1,2,b,3,cherry,c,john,a,bananas,elena}
#myset = set1|set2 | set3 | set4 
#print(myset) {1,2,b,3,cherry,c,john,a,bananas,elena}

# | only joins sets
#JOIN SET AND TUPLE
#x = {"a","b","c"}
#y = (1,2,3)
#z = x.union(y)
#print(z) #{1,2,3,a,b,c}
#x.update(y)
#print(x) {1,2,3,a,b,c}
#union() and update() will exclude any duplicate items.

#INTERSECTION (KEEPS ONLY DUPLICATES)
#set1 = {"apple","banana","cherry"}
#set2 = {"mango","cherry","crystalapple"}
#set3 = set1.intersection(set2)
#print(set3) {'cherry'}
#set3 = set1 & set2 (& is used instead of intersection)
#print(set3) {'cherry'} (& works with only same type of data set)
#set1.intersection_update(set2)
#print(set1) {'cherry'}
#set1 = {"apple", 1,  "banana", 0, "cherry"}
#set2 = {False, "google", 1, "apple", 2, True}
#set3 = set1.intersection(set2)
#print(set3){False,1,'apple'} (TRUE AND 1 IS SAME , FALSE AND 0 IS SAME)

#DIFFERENCE
#set1 = {"apple", "banana", "cherry"}
#set2 = {"google", "microsoft", "apple"}
#set3 = set1.difference(set2)
#print(set3){'banana','cherry'}
#set3 = set1 - set2 
#print(set3) {'banana','cherry'}
#set1.difference_update(set2)
#print(set1){'cherry','banana'}

#SYMMETRIC DIFFERENCE keep only the elements that are NOT present in both sets.
#set1 = {"apple", "banana", "cherry"}
#set2 = {"google", "microsoft", "apple"}
#set3 = set1.symmetric_difference(set2)
#print(set3) {google,microsoft,banana,cherry}
#set3 = set1 ^ set2
#print(set3) {google,microsoft,banana,cherry}
#set1.symmetric_difference_update(set2)
#print(set1) {google,microsoft,banana,cherry}