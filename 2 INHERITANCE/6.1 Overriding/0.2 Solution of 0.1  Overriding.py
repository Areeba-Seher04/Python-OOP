#Article: https://www.thedigitalcatonline.com/blog/2014/05/19/method-overriding-in-python/

'''
Overriding: Through method overriding a class may "copy" another class, 
avoiding duplicated code,and at the same time enhance or customize part of it.
'''

class Parent:
    def __init__(self,first,last,age):
        self.first=first
        self.last=last
        self.age=age

    def __str__(self):
        return self.first +' '+self.last+' ' +self.age
    

class Child(Parent):
    def __init__(self,first,last,age,sal):
        #Overriding : Post filtering
        super(Child,self).__init__(first,last,age)  #super() invokes the methods of parent class here __init__method of parent class
        #Parent.__init__(self,first,last,age)  
        self.sal=sal
        
    def __str__(self):
        return Parent.__str__(self)+ ' ' +str(self.sal)

obj1=Parent('james','Bond','50')
print(obj1)

obj2=Child('Rita','Bond','25',1200)
print(obj2)
