#BASIC IDEA OF CLASS AND OBJECT

class DemoClass:
    pass

my_instance_1=DemoClass()  # Constructor (constructs an object and assign a unique id to that object)  
print(type(my_instance_1)) # O/P  <class '__main__.DemoClass'>
print(id(my_instance_1))   # print the unique id of object

my_instance_2=DemoClass()  # 2nd object
print(type(my_instance_2)) 
print(id(my_instance_2))

