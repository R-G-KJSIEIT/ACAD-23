class Studentt:
    student_name = "Rishi"
    student_marks = 98
    def student(s,m):
        student_name = s
        student_marks = m

stud=Studentt()

print(stud.student_name)
print(stud.student_marks)

s = input("Enter Student name:   ")
m = input("Enter Student marks:  ")
stud.student_name = s
stud.student_marks = m

print(stud.student_name)
print(stud.student_marks)
