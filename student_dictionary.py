from xyz.supercoders.college.student import Student

student_dict = {}

def create_new_student():
	name = input("Enter name : ")
	rollno = int(input("Enter roll no : "))
	gender = input("Enter gender : ")
	marks = float(input("Enter marks"))

	s = Student(name,rollno,gender,marks)
	student_dict[rollno] = s

def search_by_rollno(rollno):
	if rollno in student_dict:
		return student_dict[rollno]

def get_males():
	return [s[1] for s in student_dict.items() if s[1].gender=="M"]

def display(student_list):
	for s in student_list:
		s.displayDetails()
while True:
	print("1. Enter student data")
	print("2. Search by roll no")
	print("3. Display males")
	print("4. Exit")
	
	c = int(input("Enter choice : "))
	
	if c==1:
		create_new_student()
	elif c==2:
		#search by rollno
		search_roll = int(input("Enter roll no to be searched : "))
		s = search_by_rollno(search_roll)
		s.displayDetails()
	elif c==3:
		males = get_males()
		display(males)
	else:
		break
