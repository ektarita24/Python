def isEven(n):
	return True if n%2==0 else False

n = int(input("Enter n : "))
print("Even") if isEven(n) else print("Odd")
