class student:
  
 def __init__ (self,name,roll_number,cgpa):
    self.name=name
    self.roll_number=roll_number
    self.cgpa=cgpa

def sort_students(student_list):
  sorted_students=sorted(student_list,
                         key=lambda student:student.cgpa,
                         reverse=True)
  return sorted_students


students=[
  student("karthika  \t","fg24\t",8.9),
  student("Meena     \t","aa24\t",9.9),
  student("kalaiselvi\t","po15\t",7.9)
]

sorted_students=sort_students(students)

for student in sorted_students:
  
  print("NAME:",student.name,
        "ROLL_NO:",student.roll_number,
        "CGPA:",student.cgpa)

