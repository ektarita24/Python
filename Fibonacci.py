n = int(input("Enter n"))

a, b = 0, 1

"""
i = 1
while i<=n:
	print(a,end='\t')
	c = a+b
	a, b = b, c
	i = i+1
"""

for i in range(0,n):
	print(a,end='\t')
	c = a+b
	a, b = b, c
