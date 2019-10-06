'''
__init__ : reserverd method in class,known as constructor in OOP. When we create
an object then this method is called and allow the class to initialize the
attributes of a class
** __init__ only return None because it is initialzer method , dont return any thing from __init__

'''

class Person:
    def __init__(self,name,age):
        self.name = name   # object variable / instance variable
        self.age = age
        print("My name is {} and I am {} years old".format(self.name,self.age))  

# Make an object and initialize it with the given argument
JOHN = Person('John',23) 

'''
self receives the ID OF JOHN, it will looks like:
	def __init__(JOHN, John, age):
		JOHN.name = John
		JOHN.age = 23
'''
print(JOHN.name) 
print(JOHN.age)
