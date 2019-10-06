class Person():           #parent
    pass

class Employee(Person):   #child of parent and parent of Programmer
    pass

class Programmer(Employee): #child of employee
    pass

def main():
    obj=Programmer()

if __name__=='__main__':
    main()
