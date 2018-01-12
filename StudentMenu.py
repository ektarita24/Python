from xyz.supercoders.college.student import Student

students = []

def create_new_student():
	name = input("Enter name : ")
	rollno = int(input("Enter roll no : "))
	gender = input("Enter gender : ")
	marks = float(input("Enter marks"))

	s = Student(name,rollno,gender,marks)
	students.append(s)

def get_count():
	return len(students)

def get_males():
	return [s for s in students if s.gender=="M"]

def get_females():
	return [s for s in students if s.gender=="F"]

def display(student_list):
	for s in student_list:
		s.displayDetails()
while True:
	print("1. Enter student data")
	print("2. Display total no. of students")
	print("3. Display males")
	print("4. Display females")
	print("5. Exit")
	
	c = int(input("Enter choice : "))
	
	if c==1:
		create_new_student()
	elif c==2:
		count = get_count()
		print("Total Students : "+str(count))
	elif c==3:
		males = get_males()
		display(males)
	elif c==4:
		females = get_females()	
		display(females)
	else:
		break
