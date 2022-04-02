from bank import Account
#import bank



rohit_acc=Account('Rohit','Ram',"RTNPR5456G",10000)
print("Your account details follows:")
print("User Name is :", rohit_acc.username)
print("Password is :", rohit_acc.password)

# rohit_acc.__amount=10000000
# print("Your balance is:",rohit_acc.__amount)
print("Balance:",rohit_acc.get_balance())
rohit_acc.set_balance(50000)
print("Balance:",rohit_acc.get_balance())
