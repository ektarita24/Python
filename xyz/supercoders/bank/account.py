from xyz.supercoders.bank.illegal_argument_error import IllegalArgumentError
from xyz.supercoders.bank.insufficient_funds_error import InsufficientFundsError

class Account:
	def __init__(self,acc_no,acc_type,balance):
		# instance attribute
		self.acc_no = acc_no
		self.acc_type = acc_type
		self.__balance = balance	# __balance => private attribute

	def set_balance(self, balance):
		if balance < 0:
			print("Please check balance")
		else:		
			self.__balance = balance		
	
	def get_balance(self):
		return self.__balance

	def withdraw(self, amount):
		print("Transaction Started")
		try:
			if amount <= 0:
				raise IllegalArgumentError('Amt cant be 0 or -ve')
			if self.__balance-amount < 0:
				raise InsufficientFundsError()
			self.__balance-=amount
		finally:
			print("Transaction Ended")
		return self.__balance

	def deposit(self, amount):
		if amount <= 0:
			raise IllegalArgumentError()
		self.__balance+=amount
		return self.__balance

	def get_details(self):
		return 'Acc No : {acc_no}\nAcc Type : {acc_type}\nBalance : {balance}'.format(acc_no = self.acc_no, acc_type = self.acc_type, balance = self.__balance) 

if __name__ == '__main__':
	a = Account(acc_no = 123,acc_type = "savings",balance=1000)
	print(a.get_details())	
	
	a.withdraw(200)
	a.deposit(300)

	a.__balance = -6000	# balance will not change since it is private.

	print(a.get_details())
