#DATATYPES 
#Text Type:	str
#Numeric Types:	int, float, complex
#Sequence Types:	list, tuple, range
#Mapping Type:	dict
#Set Types:	set, frozenset
#Boolean Type:	bool
#Binary Types:	bytes, bytearray, memoryview
#None Type:	NoneType 

#GETTING THE DATA TYPE 
#x = 5
#print(type(x)) <class 'int'>

#SETTING THE DATA TYPE
#x = "Hello World"
#print(x)
#print(type(x)) Hellow  World <class 'str'>
#x = 20
#print(x)
#print(type(x)) 20 <class int>
#x = 20.5
#print(x)
#print(type(x)) 20.5 <class 'float'>
#x = 1j
#print(x) 1j
#print(type(x)) <class complex>
#x = ["apple", "banana", "cherry"]
#print (x) ['apple', 'banana', 'cherry']
#print(type(x))<class list>
#x = ("apple","banana","cherry")
#print(x) ('apple','banana','cherry')
#print(type(x)) <class 'tuple'>
#x = range(6)
#print (x) (0,6) 
#print(type(x))<class 'range'>
#x ={"name": "Maitree" , "age": 21}
#print(x) {'name':'Maitree','age':21}
#print(type(x))<clase 'dict'>
#x = {"apple","banana","cherry"}
#print(x) {'banana','apple','cherry'}
#print(type(x)) <class 'set'>
#x = frozenset({"apple","banana","cherry"})
#print(x) ({'banana','cherry','apple'})
#print(type(x)) <class 'frozenset'>
#x = True
#print(x) True
#print(type(x)) <class 'bool'>
#x = b"Hello"
#print(x)b'Hello' 
#print(type(x)) <class 'bytes'>
#y= bytearray(5)
#print(y) bytearray(b'\x00\x00\x00\x00\x00')
#print(type(y))<class 'bytearray'>
#x = memoryview(bytes(5))
#print(x) <memory at 0x000002CB6433C7C0>>
#print(type(x)) <class 'memoryview'>
#x = None
#print(x) None 
#print(type(x)) <class 'None type'>

#Setting the Specific Data Type
#x = str("Hello World")
#print(x) ello World
#print(type(x))<class 'str>'
#x = int(20)
#print(x) 20
#print(type(x)) <class int>
#x = float(20.5)
#print(x) 20.5
#print(type(x)) <class 'float'>
#x = complex(1j)  
#print(x) 1j
#print(type(x))<class 'complex'>
#x = list(("apple", "banana", "cherry"))
#print(x)['apple','banana','cherry']
#print(type(x)) <class 'list'>
#x = tuple(("apple", "banana", "cherry"))
#print(x) ('apple','banana','cherry')
#print(type(x)) (<class 'tulip'>)
#x = range(6)		
#print (x) range(0,6)
#print(type(x)) <class 'range'>
#x = dict(name="John", age=36)	
#print(x)
#print(type(x))	
#x = set(("apple", "banana", "cherry"))	
#print(x)
#print(type(x))	
#x = frozenset(("apple", "banana", "cherry")) print(x)
#print(type(x))		
#x = bool(5)		print(x)
#print(type(x))
#x = bytes(5)		print(x)
#print(type(x))
#x = bytearray(5)	print(x)
#print(type(x))	
#x = memoryview(bytes(5))print(x)
#print(type(x))