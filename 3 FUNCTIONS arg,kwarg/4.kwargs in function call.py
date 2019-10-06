def some_kwargs(kwarg_1, kwarg_2, kwarg_3):
    print("kwarg_1:", kwarg_1)  #prints value
    print("kwarg_2:", kwarg_2)
    print("kwarg_3:", kwarg_3)

'''kwargs is a dictionary : function arg receives key from kwargs and prints its value '''
kwargs = {"kwarg_1": "Val", "kwarg_2": "Harper", "kwarg_3": "Remy"}  
some_kwargs(**kwargs)
#if key and arg are differnt error will occured
