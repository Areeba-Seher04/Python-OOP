
class Parent:
    def __init__(self,first,last,age):
        self.first=first
        self.last=last
        self.age=age

    def method(self):
        return self.first +' '+ self.last+ ' '+ str(self.age)
    

class Child(Parent):   #same arg are present in parent class (not a good attempt), violaion of DRY(dont repeat yoursef) rule
    def __init__(self,first,last,age,sal):
        self.first=first
        self.last=last
        self.age=age       
        self.sal=sal
        
    def method(self):
        return self.first+' '+self.last+ ' ' +str(self.age)+ ' ' +str(self.sal) #violaion of DRY(dont repeat yoursef) rule

obj1=Parent('james','Bond',50)
print(obj1.method())


obj2=Child('Rita','Bond',25,1200)
print(obj2.method()) 

