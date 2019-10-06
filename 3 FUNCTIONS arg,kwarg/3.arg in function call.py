#ARG IN FUNCTION CALL
#We can also use *args and **kwargs to pass arguments into functions.

def some_args(arg_1, arg_2, arg_3):
    print("arg_1:", arg_1)
    print("arg_2:", arg_2)
    print("arg_3:", arg_3)

args = ("Sammy", "Casey", "Alex")  #args is a tuple
some_args(*args)  #pass all arguments in a function

args = ("sara","yusra")
some_args("Areeba",*args)

args = [1,2] #we can also pass list
some_args(3,*args)