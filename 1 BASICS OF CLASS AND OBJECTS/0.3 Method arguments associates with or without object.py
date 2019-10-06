#METHOD ARGUMENT ASSOCIATES WITH OBJECT OR WITHOUT OBJECT

class DemoClass:
    def double_it(self,value):  
        doubled_value=value*2   #double_value is not associated with object
        return doubled_value
    
my_object1=DemoClass()   
print(my_object1.double_it(2))



class DemoClass:
    def double_it(self,value):  
        self.doubled_value=value*2  #self.double_value, double_value is associated with object
        return self.doubled_value
        
my_object2=DemoClass()
print(my_object2.double_it(2))


