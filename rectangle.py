def perimeter(length, breadth):
	return 2*(length+breadth)

def area(length, breadth):
	return length*breadth

x = int(input("Enter length : "))
y = int(input("Enter breadth : "))

p = perimeter(x,y)
print("Perimeter is : "+str(p))

a = area(x,y)
print("Area is : "+str(a))

