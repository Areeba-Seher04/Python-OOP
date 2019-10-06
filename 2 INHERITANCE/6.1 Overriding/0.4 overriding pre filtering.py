'''Customization of methods'''

class Message:
	def message(self,message):
		print(message)


class MyMessage(Message):
	def message(self,message):
		#overriding :prefiltering
		message = "You are so Smart " + message  #overriding parent class message
		super(MyMessage,self).message(message)


x = MyMessage()
x.message('Areeba.')
