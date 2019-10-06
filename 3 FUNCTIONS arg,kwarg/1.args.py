#WE CAN PASS VARIABLE NUMBER OF ARGUMENTS USING *args and **kwargs

#We use *args and **kwargs as an argument when we are unsure about the number of arguments to pass in the functions.
# *args: (Non Keyword Arguments)


'''
1. use * before the arg so you can pass variable(many) arguments
2. this arg are passed as TUPLE in a function
3. these passed arguments make tuple inside the function with same name as the parameter excluding asterisk *
'''
def Add(*num):  
	print(num)  #print tuple
	sum = 0

	for i in range (len(num)):
		sum = sum + num[i]
	print(sum)



Add(1,2,3)
Add(1,3,5,8,5,1)