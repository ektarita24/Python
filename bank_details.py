while True:
	print("1. Create account")
	print("2. Withdraw")
	print("3. Deposit")
	print("4. Display")
	print("5. Exit")

	c = int(input("Enter choice : "))

	if c==1:
		acc_no = int(input("Enter acc no.: "))
		acc_type = input("Enter acc type : ")
		balance = float(input("Enter balance : "))
		a1 = Account(acc_no,acc_type,balance)
	elif c==2:
		a1.withdraw(float(input("Enter amount to be withdrawn")))
	elif c==3:
		a1.deposit(float(input("Enter amount to be deposited")))
	elif c==4:
		print(a1.get_details())				
	else:
		break
