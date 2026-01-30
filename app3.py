from models.classroom import Classroom
from models.student import Student

oop = Classroom("OOP")
oop.add_student(Student(1, "Alice", 20, "S1001"))
oop.add_student(Student(2, "Bob", 21, "S1002")) 
oop.add_student(Student(3, "Charlie", 22, "S1003"))
print(f"{oop.name} has {len(oop)} students")  
print("students in classroom:")
for i in range(len(oop)):
    print(oop[i])