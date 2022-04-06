class BankAccount:
    bank_name = "Doja Bank" #pulled from learn platform under @classmethod 
    all_accounts = [] #pulled from learn platform under @classmethod
    # don't forget to add some default values for these parameters!
    def __init__(self, balance, int_rate): 
        self.balance = balance
        self.int_rate = int_rate
    def deposit(self, amount):
        self.balance += (amount)
        return self
    def withdrawl(self, amount):
        self.balance -= (amount)
        return self
    def display_account_info(self):
        print(f"BankAccount: ${self.balance}")
        return self
    def yield_interest(self):
        self.balance = self.balance + (self.balance * self.int_rate) #tried to use yield_interest instead, but realized -> I should be calling what's in the __init__ for the program instead. - was yeilding float/method errors
        return self

adamAccount = BankAccount(500, .15)
jasonAccount = BankAccount(2000, .05)

adamAccount.deposit(2000).deposit(400).deposit(50).withdrawl(800).yield_interest().display_account_info()
jasonAccount.deposit(7000).deposit(10).withdrawl(3400).withdrawl(30).withdrawl(65).withdrawl(800).yield_interest().display_account_info()


# tried to pull this off of the @classmethod section of the learn platform, but i don't think it works. It didn't break the code.. yay? 
@classmethod
def all_balances(cls):
    sum = 0
    for balance in cls.all_accounts:
        sum += balance
    return sum
#======================================================================
# Starting over  ⬆
#======================================================================



#======================================================================
# March Python 2022 failed attempt  ⬇
#======================================================================



    # def deposit(self, amount):
    #     self.amount += amount
    #     print("You deposited: ", amount)

    # def withdraw(self, amount):
    #     self.amount -= amount
    #     print("Withdrawal amount: ", amount)

    # def display_account_info(self):
    #     print(f"Account Balance: ${balance}")

    # def yield_interest(self):
    #     self.amount *= amount
    #     print("Interest Rate: ", amount)



