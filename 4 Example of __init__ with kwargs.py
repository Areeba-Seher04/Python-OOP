# Prerequisit : Understanding of kwargs and dictionary

''' this program allows user to only initilize the class with predefined attributes
otherwise it will throw an error (Invalid argument in contructor)
'''

class Bar:
        def __init__(self, **kwargs):
                #predefine attributes with default values
                self.a = 0
                self.b = 0
                self.A = True
                self.B = True

                #get a list of all predefined keys
                allowed_keys = list(self.__dict__.keys())
                print(allowed_keys)

                #update dictionary only for predefined keys
                #ignoring others
                for key , value in kwargs.items():
                        if key in allowed_keys:
                                #update takes typle inside list or takes dictionar
                                #update , update the value with respect to key
                                self.__dict__.update([(key,value)])
                print("new",self.__dict__.items())

                #to Not silently ignoring the others
                rejected_keys = set(kwargs.keys()) - set(allowed_keys) #sets can be subtracted
                if rejected_keys:
                        raise ValueError("Invalid arguments in constructor:{}".format(rejected_keys))
                        



#x=Bar(a=1,b=2,A=3,n=4) # error

x=Bar(a=1,b=2,A=3)  #update the predefined values with new one

y = Bar()  #print all predefined values

#all variables associate to function is saved in __dict__
print("predefined var dict",x.__dict__.keys())

#x={'areeba','seher}
#x.update({'areeba','seher'}) #update the value where key is areeba

