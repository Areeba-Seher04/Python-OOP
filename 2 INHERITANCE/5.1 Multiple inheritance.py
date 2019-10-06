class A:
    def m(self):
        print('m() from class A ...')

class B:
     def m(self):
        print('m() from class B ...')

class C(B,A):      #First check the C then it will chec a/c to the order of the class
#class C(A,B):
        pass


def main():
    o=C()
    o.m()

if __name__=='__main__':
    main()
