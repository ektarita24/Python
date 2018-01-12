class Book:
	def __init__(self,book_id, title = "NA", pages = 1, price = 0):
		self.book_id = book_id
		self.title = title
		self.pages = pages
		self.price = price

	@property
	def title(self):
		return self.__title

	@title.setter
	def title(self, title):
		if title is None or len(str(title)) == 0:
			print('Title Required') 
		else:
			self.__title = title

	@property
	def price(self):
		return self.__price

	@price.setter
	def price(self, price):
		if price is None or int(price)<0:
			print("Price cannot be negative") 
		else:
			self.__price = price
		
	@property
	def pages(self):
		return self.__pages

	@pages.setter
	def pages(self, pages):
		if pages is None or int(pages)<=0:
			print("Pages have to be 1 or greater than it") 
		else:
			self.__pages = pages
				

	def get_details(self):
		return 'Id : {book_id}\tTitle : {title}\tPages : {pages}\tPrice : {price}\n'.format(book_id = self.book_id, title = self.title, pages = self.pages, price = self.price)

	def is_free(self):
		return True if self.price == 0 else False

if __name__ == '__main__':
	b1 = Book('B1')
	b2 = Book('B2','Book 2',24,100)
	
	print(b1.get_details())
	print(b2.get_details())
	
	print('Free') if b1.is_free() else print('Not Free')
		
	print('Free') if b2.is_free() else print('Not Free')
		
	
