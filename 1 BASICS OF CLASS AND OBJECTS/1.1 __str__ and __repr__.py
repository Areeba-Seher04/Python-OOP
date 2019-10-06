# https://www.journaldev.com/22460/python-str-repr-functions
'''
__str__  reserverd method in class returns the string representation of object
__repr__ reserverd method in class returns the object represenation.It could be any valid python expression such as tuple, dictionary, string etc.
'''
class Person:
    def __init__(self, personName, personAge):
        self.name = personName
        self.age = personAge

    def __repr__(self):
        #return {'name':self.name, 'age':self.age}
        return '{name:'+self.name+', age:'+str(self.age)+ '}' #return string

Areeba = Person("Areeba",100)
'''
if __str__ method is present ,call __str__ if not then call __repr__ but __repr__ should
return STRING
'''
print(Areeba)

#*---------------------------------------------------------------------------------------------
#if __str__ and __repr__both are present then __repr__ can return any object representation

class Person1:
    def __init__(self, personName, personAge):
        self.name = personName
        self.age = personAge

    def __repr__(self):
        return {'name':self.name, 'age':self.age} #return dictionary
        #return '{name:'+self.name+', age:'+str(self.age)+ '}' #return string

    def __str__(self):
        return 'name:' + self.name + ' age:' + str(self.age)

Areeba = Person1("Areeba",100)
print(Areeba) #__str__ method will call
print(Areeba.__str__())
print(Areeba.__repr__()) 
print(type(Areeba.__repr__()))  #type:__dict__



