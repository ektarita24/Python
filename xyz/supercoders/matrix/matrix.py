class Matrix:
	def __init__(self,rows,columns,elements):
		self.rows = rows
		self.columns = columns
		self.elements = elements

	@property
	def rows(self):
		return self.__rows

	@rows.setter
	def rows(self, rows):
		if rows < 0:
			print("Rows cannot be negative")
		else:
			self.__rows = rows

	@property
	def columns(self):
		return self.__columns

	@columns.setter
	def columns(self, columns):
		if columns < 0:
			print("Columns cannot be negative")
		else:
			self.__columns = columns

	def get_matrix(self):
		s = ""
		for r in range(0,self.rows):
			for c in range(0,self.columns):
				s += "{element} ".format(element = self.elements[r][c])
			s +="\n"
		return s

	def add_matrix(self,m2):
		parent = []
		for e1,e2 in zip(self.elements,m2.elements):
			child = [(ie1+ie2) for ie1,ie2 in zip(e1,e2)]
			parent.append(child)
		return Matrix(self.rows,self.columns,parent)

	def transpose_matrix(self):
		parent = [list(element) for element in zip(*self.elements)]
		return Matrix(self.columns,self.rows,parent)

	def multipy_matrix(self,m2):
		parent = []
		for r in range(0,self.rows):
			child = []
			for c in range(0,m2.columns):
				sum = 0
				for k in range(0,self.columns):
					sum += self.elements[r][k]*m2.elements[k][c]
				child.append(sum)
			parent.append(child)
		return Matrix(self.rows,self.columns,parent)
	
if __name__ == '__main__':

	m1 = Matrix(2,3,[[1,2,3],[4,5,6]])
	print(m1.get_matrix())
	print(m1.transpose_matrix().get_matrix())
	m1.rows = -2
	print(m1.rows)	
"""
	rows = int(input("Enter rows : "))
	cols = int(input("Enter cols : "))
	parent = []
	
	for r in range(0,rows):
		child = []
		for c in range(0,cols):
			element = int(input('Enter element ({row_no},{col_no}) : '.format(row_no=r,col_no=c)))
			child.append(element)
		parent.append(child)
	
	m1 = Matrix(rows,cols,parent)
	print(m1.get_matrix())

	rows = int(input("Enter rows : "))
	cols = int(input("Enter cols : "))
	parent = []
	
	for r in range(0,rows):
		child = []
		for c in range(0,cols):
			element = int(input('Enter element ({row_no},{col_no}) : '.format(row_no=r,col_no=c)))
			child.append(element)
		parent.append(child)
	
	m2 = Matrix(rows,cols,parent)
	print(m2.get_matrix())

	print("Addition")
	#m3 = m1.add_matrix(m2)
	#print(m3.get_matrix())

	print("Transpose")
	m4 = m1.transpose_matrix()
	print(m4.get_matrix())

	print("Multiplication")
	#m5 = m1.multipy_matrix(m2)
	#print(m5.get_matrix())
"""
