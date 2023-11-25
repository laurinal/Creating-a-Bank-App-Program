# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 11:48:39 2023

@author: lEO
"""

while True:
    accounts = []
    class Account:
        bank_name = 'Leon Bank of Nigeria'
        def __init__(self, name):
            self.account_number = 10001
            for number in accounts:
                if self.account_number == number:
                    self.account_number = self.account_number + 1
                    accounts.append(self.account_number)
                    self.__account_balance = float(0)
                    self.holder = name
                else: 
                    accounts.append(self.account_number)
                    self.__account_balance = float(0)
                    self.holder = name
            
        def deposit(self, amount):
            self.amount = float(amount)
            self.__account_balance = self.__account_balance + self.amount
            print('Success')
            
        def withdrawal(self, amount):
            self.amount = float(amount)
            if self.amount > self.__account_balance or (self.__account_balance - self.amount) <= 500: 
                print('Insufficient Funds')
            else:
                self.__account_balance = self.__account_balance - self.amount
                print('Transaction Successful')
        
        def check_balance(self):
            return self.__account_balance
        
    
    person1 = Account('Onyiriuba Leonard')
    person2 = Account('Agnes')
    person3 = Account('Lara')
    
    print(person2.deposit(12000.67882))
    print(person1.bank_name)

    