class Contact:
	def __init__(self, email, mobile = None, fax = None):
		self.email = email
		self.mobile = mobile
		self.fax = fax

	def get_details(self):
		details_str = ""
		if not self.email is None:
			details_str += 'Email : {0}\n'.format(self.email)

		if not self.mobile is None:
			details_str += 'Mobile : {0}\n'.format(self.mobile)

		if not self.fax is None:
			details_str += 'Fax : {0}\n'.format(self.fax)

		return details_str

if __name__ == '__main__':
	c1 = Contact('abc@gmail.com')
	print(c1.get_details())

	c2 = Contact('abc@gmail.com','1234567890')
	print(c2.get_details())

	c3 = Contact(None)
	print(c3.get_details())
