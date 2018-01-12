from person import Person
from book import Book
from salaried_individual import SalariedIndividual
from salary_calculator import SalaryCalculator

class Professor(Person, SalariedIndividual):
	
	prof_tax = 200 
	def __init__(self, name, gender, subjects = [], email = None,mobile = None,fax = None, working_days = 0, cost = 0):
		super().__init__(name, gender, email, mobile, fax)
		self.subjects = subjects
		self.working_days = working_days
		self.cost = cost
		
	def get_details(self):
		str = super().get_details()		
		str += "Subjects : {0}".format(self.subjects)
		return str

	def get_no_of_days(self):
		return self.working_days
	
	def get_cost_per_day(self):
		return self.cost
	
	def get_tax(self):
		return Professor.prof_tax


if __name__ == '__main__':
	p = Professor(name = 'Ekta', gender = 'F', subjects=["Maths","French"], working_days=15, cost=2000)
	print(SalaryCalculator.calc_salary(p))	
	'''
	print(p)
	PhotoSession.take_photo(p)

	b1 = Book('B1')
	b2 = Book('B2','Book 2',24,100)

	#print(p.get_details())
	p.issue_book(b1)
	p.issue_book(b2)

	#print(p.get_books_issued_details())
	'''
