class Add:
	def SUM(self,x,y): 
		self.x = x
		self.y = y
		return self.x + self.y
		

class AddThreeNumber(Add):
	def SUM(self,x,y):
		twoNumberSum = super(AddThreeNumber,self).SUM(x,y)
		return twoNumberSum + 10


x = AddThreeNumber()
print(x.SUM(1,2))


