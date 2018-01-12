from student import Student
from professor import Professor

class PhotoSession:

	def take_photo(individual):
		if not (isinstance(individual,Student) or isinstance(individual,Professor)):
			print("Cannot take photo")
		else:
			print("Name : {0}\tGender : {1} has clicked a photo".format(individual.name,individual.gender))
			if isinstance(individual,Student):
				print("Roll no : {0}".format(individual.rollno))
	
if __name__=='__main__':	
	p = Professor(name = 'Ekta', gender = 'F', subjects=["Maths","French"])
	PhotoSession.take_photo(p)

	s = Student("ABC",1,"M",98)
	PhotoSession.take_photo(s)

	PhotoSession.take_photo(5)
