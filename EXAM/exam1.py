usersname = str(input("enter your name: "))

surname = str(input("enter your surname: "))

cardtype = str(input("enter your type of card: "))

s = "s"

fullname = [usersname,surname]

print(fullname,s) 

print("bank account has been created.")

a = int(input("enter the amount of money you would like to deposit: "))

c = "you are good to go, have a nice day"

d = int(input("enter the amount of money you would like to withdraw: "))

bank_balance = "your bank balance is:" 

bank_balance2 = a

after_withdrawal = bank_balance2 - d
bank_list2 = [ bank_balance, after_withdrawal, c]

print(bank_list2)

