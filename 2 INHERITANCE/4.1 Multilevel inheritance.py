class Person():           #parent
   def assign_basic(self,name,age):
       self.name=name
       self.age=age

class Employee(Person):   #child of Person and parent of Programmer
    def assign_emp(self,idno):
        self.idno=idno

class Programmer(Employee): #child of employee
    def assign_prog(self,lang):
        self.lang=lang

class Demo(Programmer):
    pass

def main():
    o=Demo()          #this obj can access parent class and parent of parent class
    o.assign_basic('Areeba',45)
    o.assign_emp(123)
    o.assign_prog('Python 3')
    print(o.name,o.age,o.idno,o.lang)

if __name__=='__main__':
    main()


#Multilevel Inheritance: Demo can access its parent class and parent of parent class
#but first it search for a method in its own class then in parent class and in last parent of the parent class