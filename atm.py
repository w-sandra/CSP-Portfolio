#Sandra
#defines a function 3 functions that simulate transactions in an atm

balance= 100
def deposit(amount):
    global balance
    balance= amount + balance
    print("deposite succesful")

def withdraw(amount):
    global balance
    balance= balance - amount
    print("withdraw succesful")

def display_total():
    print(f"balance = {balance}")

#Main
deposit(50)
withdraw(30)
display_total()
