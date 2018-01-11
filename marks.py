def calculateGrade(m):
	if m>=70 and m<=100:
		return "A"
	elif m>=60 and m<70:
		return "B"
	elif m>=40 and m<60:
		return "C"
	elif m>=0 and m<40:
		return "F"
	else:
		return "I"

m = int(input("Enter marks : "))
print(calculateGrade(m))

