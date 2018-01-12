from xyz.supercoders.bank.account import Account
from xyz.supercoders.bank.illegal_argument_error import IllegalArgumentError
from xyz.supercoders.bank.insufficient_funds_error import InsufficientFundsError

a = Account(acc_no = 123,acc_type = "savings",balance=1000)
print(a.get_details())	

amt = input("Enter amount to withdraw : ")
try:	
	amount = float(amt)
	updated_bal = a.withdraw(amount)
except ValueError:
	print("Enter correct value")
except IllegalArgumentError as iae:
	print(iae)
	print("Enter valid amount")
except InsufficientFundsError:
	print("Funds are less to withdraw")

else:
	print("New Balance : "+str(updated_bal))

amt = input("Enter amount to deposit : ")
try:	
	amount = float(amt)
	updated_bal = a.deposit(amount)
except ValueError:
	print("Enter correct value")
except IllegalArgumentError:
	print("Enter valid amount")

else:
	print("New Balance : "+str(updated_bal))

	


