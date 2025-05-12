"""
Let's Practice

Create Account class with 2 attributes - balance & account no.
Create methods for debit, credit & printing the balance.


"""

class Account:
    balance=None
    Account_no=None


    def __init__(self,balance,Account_no):
        self.balance=balance
        self.Account_no=Account_no


    def debit(self,mon):
        self.balance-=mon
        

    def credit(self,mon):
        self.balance+=mon

    def print(self):
        print(self.Account_no," Account number the balnce is ",self.balance)


A1=Account(1000,8393)
A1.credit(200)

A1.print()
A1.debit(500)
A1.print()