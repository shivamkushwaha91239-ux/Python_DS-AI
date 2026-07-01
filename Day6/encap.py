#define a class name
class Bank:
 
 #constructor: atumatically called when an object of the class is created
  def __init__(self):
    #private attribute: can be accessed only within the class
    #initial balance of the account is set to 5000
    #double underscore(__) before the attribute name makes it private
    self.__balance = 5000 # private attribute 

#created a method to deposit money into the account
  def deposit(self, amount):
        #add deposit money to the account
     self.__balance += amount # add the amount to the balance

 # display the current balance of the account
  def show_balance(self):
        #print the current balance of the account
     print("Current Balance:", self.__balance) # display the balance      

#create an object of the Bank class
b = Bank() # create an object of the Bank class
b.deposit(2000) # deposit 2000 into the account
b.show_balance() # display the current balance of the account  
