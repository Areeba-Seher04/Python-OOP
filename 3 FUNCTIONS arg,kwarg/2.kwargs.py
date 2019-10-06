'''
** kwargs pass keyword argument to function  (dictionary type)
** In the function, we use the double asterisk ** before the parameter name
** The arguments are passed as a dictionary
** these arguments make a dictionary inside function with name same as the parameter excluding double asterisk **.
'''

def intro(**data):
	print(data)   #prints dictionary {'Name':'Areeba'}
	for key , value in data.items(): #data.items(): dict_items([('name', 'areeba')]
		print("{} is {}".format(key,value))

intro(Name = "Areeba")  #Name is key and Areeba is value
intro(Name="areeeba",job = "student")






#Ordering Arguments (param,*arg,**kwargs)
def all_three(param,*arg,**kwargs):
	print("param",param)
	print("*arg",arg)
	print("**kwargs",kwargs)


all_three(12,23,45,56,name="Areeba",data=1998)
''' RESULT
param 12
*arg (23, 45, 56)
**kwargs {'name': 'Areeba', 'data': 1998}'''









