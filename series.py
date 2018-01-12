def fiboSeries(n):
	a, b = 0, 1
	for i in range(0,n):
		print(a,end='\t')
		c = a+b
		a, b = b, c

def multipleOf3Series(n):
	for i in range(1,n+1):
		for s in range(1,i):
			print(" ", end='')
		print(3*i)
"""
Below code is executed only when module is run directly
When we import the module it will not be executed
"""
if __name__ == "__main__":
	n = int(input("Enter n"))
	fiboSeries(n)


