print("Before")

n = input("Enter n : ")
try:
	ni = int(n)
except ValueError:
	print("Enter correct value")
else:
	print(ni)

print("After")
