#import series
import math # built in module
import xyz.supercoders.custom.math as mo # custom module
from series import fiboSeries,multipleOf3Series as mo3

print(math.pi)
while True:
	print("1. Fibonacci Series")
	print("2. Series of 3")
	print("3. Even or Odd")
	print("4. Exit")
	
	c = int(input("Enter choice : "))
	
	if c==1:
		n = int(input("Enter n"))
		fiboSeries(n)
		
	elif c==2:
		n = int(input("Enter n"))
		mo3(n)
	elif c==3:
		n = int(input("Enter n"))
		mo.isEven(n)		
	else:
		break
