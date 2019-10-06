class Account:
    def __init__(self,name,balance):
        self.name=name                 
        self.balance=balance

    def debit(self,withdrawl):
         self.balance=self.balance-withdrawl

    def credit(self,deposit):
         self.balance=self.balance-deposit
         
    def set_name(self,name):
         self.name=name
         
    def get_balance(self):           
         return self.balance
        
    def get_name(self):             
         return self.name
        
Customer=Account('Rita',100)
print('Name: ',Customer.get_name(),'\n','Balance: ',Customer.get_balance())
Customer.debit(20)
print('Name: ',Customer.get_name(),'\n','Balance: ',Customer.get_balance())
Customer.credit(45)
print('Name: ',Customer.get_name(),'\n','Balance: ',Customer.get_balance())
Customer.set_name('jones')
print('Name: ',Customer.get_name(),'\n','Balance: ',Customer.get_balance())
