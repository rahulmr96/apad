
class BankAccount(object):
    
    def __init__(self,val=5):
        self.balance=val
    

    def deposit(self,amount):
        self.balance+=amount
    
    def withdraw(self,amount):
        if(self.balance>=amount):
            self.balance=self.balance-amount
            return self.balance
        else:
            return "Dude you don't have enough money"

    def get_balance(self):
        return self.balance
    
    def quarterly_interest(self):
        self.balance=self.balance*1.07/4
