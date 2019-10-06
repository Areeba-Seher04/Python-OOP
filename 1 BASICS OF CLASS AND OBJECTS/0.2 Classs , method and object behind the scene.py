# CLASS , OBJECT AND METHOD BEHIND THE SCENE

'''
**object=CLass(): when class is called then an OBJECT is associated with that CLASS
**object.method(): msg will send to that OBJECT to execute method and self received the ID of 
  that object
**SELF RECIEVE THE ID OF THE OBJECT: after running the programm you observed that the id of 
  the object and id of the self is same as self receives the id of object
'''

class DemoClass:
    def demo_method(self):       #method or behaviour (piece of code)
        print("I am a method containing id of the object {}".format(id(self)))

my_object=DemoClass()    # constructor  (construct an object)
my_object.demo_method()  # object.method (msg will send to object to execute method (behaviour))
print("id of object:",id(my_object))

my_object1=DemoClass()    
my_object1.demo_method() 
print("id of object:",id(my_object1))

