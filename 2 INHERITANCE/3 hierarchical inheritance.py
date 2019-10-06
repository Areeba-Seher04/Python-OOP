'''In Inheritance object search for method in its own class and then in parent class'''

class A:
  def m(self):
      print('m() from class A...')

class B(A):      
    def m(self):
      print('m() from class B...')

class C(A):   #B and C are the childs of parent class (hierarchical inheritance)
     def m(self):
       print('m() from class C...')


class D(B,C):   #D is the child class of B and C (Multiple inheritance)
     def m(self):
       print('m() from class D...')
       A.m(self)
       B.m(self)
       C.m(self)

def main():
    o=D()
    o.m()

if __name__=='__main__':
    main()
