class MyOwnException(Exception):
	pass

print("Before")

n = input("Enter n : ")
try:
	ni = int(n)
	if ni < 0:
		raise MyOwnException()
except ValueError:
	print("Enter correct value")
except MyOwnException:
	print("Enter positive value")
else:
	print(ni)

print("After")
