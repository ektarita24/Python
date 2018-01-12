"""
This will have the class definition for Student
"""
from person import Person
from contact import Contact
from book import Book

class Student(Person):
	count = 0  #Class attribute
	
	def __init__(self,name,rollno,gender,marks,email = None,mobile = None,fax = None):
		super().__init__(name, gender, email, mobile, fax)
		self.rollno = rollno
		self.marks = marks
		
		Student.count += 1

	def get_details(self):
		str = super().get_details()
		str += 'Roll No : {0}\nMarks : {1}'.format(self.rollno,self.marks)		
		return str

	def calculateGrade(self):
		if self.marks>=70 and self.marks<=100:
			return "A"
		elif self.marks>=60 and self.marks<70:
			return "B"
		elif self.marks>=40 and self.marks<60:
			return "C"
		elif self.marks>=0 and self.marks<40:
			return "F"
		else:
			return "I"

	def getCount():
		return Student.count

	def get_name_roll(self):
		return (self.name,self.rollno)

if __name__ == '__main__':

	b1 = Book('B1')
	b2 = Book('B2','Book 2',24,100)
	b3 = Book('B3','Book 3',64,500)
	b4 = Book('B4','Book 4',89,900)	

	s = Student("ABC",1,"M",98)
	print(s)
	print(s.get_details())
	
	s1 = Student("ABC",1,"M",98,"abc@gmail.com","1234567890")
	print(s1.get_details())
	s1.issue_book(b1)	
	s1.issue_book(b2)
	s1.issue_book(b3)
	
	s1.return_book(b2)
	s1.issue_book(b4)
	s.return_book(b1)
	print(s.get_books_issued_details())
	print(s1.get_books_issued_details())

	
	
"""	
	t = s.get_name_roll()
	print(t[1])

	for e in t:
		print(e)
"""
