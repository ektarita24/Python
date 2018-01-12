from contact import Contact
from book import Book

class Person:

	def __init__(self,name,gender,email = None,mobile = None,fax = None):
		self.name = name
		self.gender = gender
		if not email is None or not mobile is None or not fax is None:
			self.contact = Contact(email,mobile,fax)
		else:
			self.contact = None
		self.books_issued = []
		
	def get_details(self):
		display_str = 'Name : {0}\nGender : {1}\n'.format(self.name,self.gender)
		
		if not self.contact is None:
			display_str += self.contact.get_details()
		return display_str

	def issue_book(self, book):
		self.books_issued.append(book) if len(self.books_issued)<3 else print("Cannot issue book")

	def return_book(self, book):
		index_to_remove = -1
		if len(self.books_issued) != 0:
			for index,b in enumerate(self.books_issued):
				if b is book:
					index_to_remove = index
					break
			if index_to_remove != -1:
				self.books_issued.pop(index_to_remove)
			else: 
				print("Book not issued")
		else:
			print("Books are not issued")	
	
	def get_books_issued_details(self):
		book_details = ""
		for book in self.books_issued:
			book_details += book.get_details() + '\n'
		return book_details if len(self.books_issued) > 0 else 'No Books Issued'

	def __str__(self):
		return 'Name : {0}\nGender : {1}'.format(self.name,self.gender)
