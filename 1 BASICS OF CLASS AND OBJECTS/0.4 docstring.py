# Print all the documents present in the program.

'This is docstring section for this file'

class Point:
    'This is a docstring for class Point'

    def __init__(self,x,y,z):
        'This is intializer method for class Point'
        self.assign(x,y,z)
       
    def assign(self,x,y,z):
        'This method assign the value to the co-ordination of point'
        self.x=x
        self.y=y
        self.z=z

    def printpoint(self):
        'This method assign the value to the co-ordination of point'
        print(self.x,self.y,self.z)

p1=Point(1,2,0)
print(__doc__)          #print the document part outside the class
print(Point.__doc__)    #print doc part of class
print(p1.__init__.__doc__) #print doc part of __init__
print(p1.assign.__doc__)
print(p1.printpoint.__doc__)

#--------------------------------------------------------------------------------------------------------------------
