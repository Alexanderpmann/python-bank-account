# class User:
#     def __init__(self,name):
#         self.name = name
#         self.amount = 0
#     # adding the deposit method

#     def make_deposit(self,amount):
#         self.amount += amount

#     def make_withdrawal(self,amount):
#         self.amount -= amount

#     def display_user_balance(self):
#         print(f"User: {self.name}, Balance: ${self.amount}")

#     def transfer_money(self,amount,user):
#         self.amount -= amount
#         user.amount += amount
#         self.display_user_balance()
#         user.display_user_balance()

# Waldo = User('Waldo')
# Mickey = User('Mickey Mouse')
# Minnie = User('Minnie Mouse')

# Waldo.make_deposit(100)
# Waldo.make_deposit(200)
# Waldo.make_deposit(50)
# Waldo.make_withdrawal(45)
# Waldo.display_user_balance()

# Mickey.make_deposit(1000)
# Mickey.make_deposit(1000)
# Mickey.make_withdrawal(500)
# Mickey.make_withdrawal(300)
# Mickey.display_user_balance()

# Minnie.make_deposit(1500)
# Minnie.make_withdrawal(1000)
# Minnie.make_withdrawal(5000)
# Minnie.make_withdrawal(3000)
# Minnie.display_user_balance()

# Minnie.transfer_money(500, Mickey)

# example above to work off of for this assignment


class User:
        def __init__(self,name):
        self.name = name
        self.amount = 0

