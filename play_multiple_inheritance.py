class A:
	def fun(self):
		print("Fun of A")

class B:
	def fun(self):
		print("Fun of B")

class C(A,B):
	pass

c = C()
c.fun()
