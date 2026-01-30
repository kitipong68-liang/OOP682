from models.person import person

class Student(Person):
    def __init__(self, pid, name, age, student_id):
        super().__init__(pid, name, age)
        self.student_id = student_id

    def __str__(self):
        return f"{super().__str__()}, Student ID: {self.student_id}"
