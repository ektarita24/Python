n = int(input("Enter n"))

"""
i = 1
while i<=n:
	s = 1
	while s<=i-1:
		print(" ", end='')		
		s = s+1
	print(str(3*i))
	
	i = i+1
"""

for i in range(1,n+1):
	for s in range(1,i):
		print(" ", end='')
	print(3*i)	
	
