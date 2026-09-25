class BankAccount :

    account_count=0

    def __init__(self,name,email,balance):
        self.name=name
        self._balance=balance
        self.email=email
        BankAccount.account_count += 1

    def deposite(self,money):
        if money >0: 
            self._balance +=money
            print(f" {money} deposited successfully ")
        else:
            print("balance should be possitive")

            
    def withdraw (self,money):
        if money<= 0:
            print("balance shoud be positive and greater than 0")  

        elif money > self.balance:
            print ("No enough money")

        else:
            self._balance -=money
            print (f"{money} withdrawn successfully. New balance: {self._balance}")

    @property
    def balance(self):
        return self._balance
        
    @balance.setter
    def balance(self,newbalance):
        self._balance = newbalance
        if newbalance < 0:
            print("you can't set negative balance")


def display_account(self):
        print("\n================ Account Info ================")
        print(f"Name: {self.name}")
        print(f"Name: {self.email}")
        print(f"Name: {self.balance}")
        print("\n==============================================")
                


                
accounts = []
def create_account():
        print("===========create acccount=============")
        name = input("enter your name")
        balance=float(input("enter your balance")) 
        email=input("enter your email")
        account =BankAccount(name,email,balance)
        accounts.append(account)
        print("\n   Account Created Successfully  ")


def show_account():
        if len(accounts)==0:
            print("\n No Accounts Yet! \n")
            return
        for account in accounts:
            accounts.display_account()  

def choose():
     if len(accounts)==0:
          print("\n No Accounts Yet! \n")
          return

     print(" available accounts : ")

     for index , account in enumerate(accounts):
          print(f"{index+1} {account.name}")

     choise = int(input("choose account :"))
     if choise <1 or choise >len (accounts):
               print("invalid")
               return None
     return accounts[choise-1]
    
          

             
                     
account1=BankAccount("ali","ali@gmail.com",45000)
account2=BankAccount("khaled","khaled@gmail.com",100000)

# account1.deposite(20000)
# print(account1.balance)   # 65000

# account1.balance=80     
# print(account1.balance)    #80

# account1.balance=-100       # warnning

# print(account2.balance)
# account2.withdraw(60000)
# account2.withdraw(40000)

ali=BankAccount("ali","ali@gmail.com",45000)
khaled=BankAccount("khaled","khaled@gmail.com",100000)

print(BankAccount.account_count)


