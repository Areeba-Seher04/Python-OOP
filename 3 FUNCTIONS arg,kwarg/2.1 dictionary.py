#we can not access dictionary using indexing

dict = {'name':'areeba','age':100} #{key:value}

#access by key word
dict['name']   #returns its value : areeba

#print all keys
dict.keys()  #returns : dict_keys(['name', 'age'])

#print all values
dict.values()  #returns : dict_values(['areeba', 100])

#print both keys and values
dict.items()  #returns: dict_items([('name', 'areeba'), ('age', 100)])


#iterating keys
for i in dict.keys():     #dict.keys() : list
	print(i)              #result : name (1st iterating) , age (2nd) 


#iterating values
for i in dict.values():  #dict.values() : list
	print(i)       		 #result : areeba (1st iterating) , 100 (2nd) 


for i in dict.items():   #dict.items: list of tuples
	print(i)            #result  ('name', 'areeba') and ('age', 100)


#method to access elements in tuples inside list
for key, value in dict.items():   #1st elment from tuple goes into key and 2nd one in value
	print(key,':',value)          #name:areeba , age:100   


x = [('name','areeba','seher'),(12,23,45)]   
for i , m , n in x:  ##take one tuple at a time and maps its with i ,m and n
	print(i)
	print(m)
	print(n)

#**********************************UPDATE DICTIONARY*********************************************
#https://www.programiz.com/python-programming/methods/dictionary/update
'''
The update() method adds element(s) to the dictionary 
if the key is not in the dictionary. If the key is in the dictionary,
 it updates the key with the new value.
 '''
 #syntax dict.update([other])
 #parameters: either take dictionary or iterable element key value pair (tuple)
 d = {1: "one", 2: "three"}
 d.update({1: "areeba"})  #update the value where key is 1 {key:updated_value}

d.update({3: "bhola"})  # update the key three but it is not present sin original so add it


#update with iterable
d1 = {"pappa": "Tariq"}
d1.update(x = "Ammi")


#update with tuple
d2 = {1: "one", 2: "three"}
d2.update([(4,"four"),(1, "updated_one")])








