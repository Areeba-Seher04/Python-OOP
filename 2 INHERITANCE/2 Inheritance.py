#class Person(object):
class Person:                       #Parent class    
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

class Employee(Person):           #Child class
    '''
    **Child class of Person Class
    **can access all functions and variables of Parent class
    '''
    pass

def main():
    Person_object=Person("Areeba",100)
    print("My name is {} and I am {} years old".format(Person_object.get_name(),Person_object.get_age()))
    

    Employee_object=Employee("Employee",200)   #can access all functions and variables of Parent Class
    print("My name is {} and I am {} years old".format(Employee_object.get_name(),Employee_object.get_age()))
    
    print(issubclass(Employee,Person))    #is Employee ,the subclass (child) of person?
    print(issubclass(Employee,object))    #every class in python is the subclass of object
    print(issubclass(Employee,object))
    
main()
