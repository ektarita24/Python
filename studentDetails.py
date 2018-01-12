#import student_ops as so
from xyz.supercoders.college.student import Student

name = input("Enter name : ")
rollno = int(input("Enter roll no : "))
gender = input("Enter gender : ")
marks = float(input("Enter marks : "))

print(Student.count)
s1 = Student(name,rollno,gender,marks)

"""
s1.name = input("Enter name : ")
s1.rollno = int(input("Enter roll no : "))
s1.gender = input("Enter gender : ")
s1.marks = float(input("Enter marks : "))
"""
name = input("Enter name : ")
rollno = int(input("Enter roll no : "))
gender = input("Enter gender : ")
marks = float(input("Enter marks : "))

s2 = Student(name,rollno,gender,marks)
print(Student.getCount())

s1.displayDetails()
print("Grade : "+s1.calculateGrade())

s2.displayDetails()
print("Grade : "+s2.calculateGrade())

print(s1.count) # Access class attribute using object name also but avoid using it
"""
s2.name = "ABC"
s2.rollno = 2
s2.gender = "M"
s2.marks = 89

print(s1.name)
print(s2.name)

so.display(name,rollno,gender,marks)

print("Grade : "+so.calculateGrade(marks))
"""
