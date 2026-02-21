# encapsulation

class BankAccount:
    def __init__(self,name,number,balance):
        self.name = name
        self.__number = number
        self.__balance = balance
    def deposit(self): #setter
        money = int(input("Deposit how much? £"))
        self.__balance += money
    def withdraw(self): #setter
        money = int(input("Withdraw how much? £"))
        if money > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= money
    def show_balance(self): #getter
        return self.__balance

#bank_account = BankAccount("Emma","012345",0)
#bank_account.deposit()
#bank_account.withdraw()
#print(bank_account.show_balance())

class User:
    __password = "123"
    def __init__(self,username,email):
        self.username = username
        self.email = email
    def set_password(self):
        self.__password = input("Password: ")
    def get_password(self):
        return self.__password


user = User("Alex","helloimalex@gmail.com")
print(user.get_password())
user.set_password()
print(user.get_password())