<<<<<<< HEAD
def main():
    print("Hello from fast-api-lap!")


if __name__ == "__main__":
    main()
=======
from models.student import Student
from models.staff import Staff
from models.person import Person

def main():
    person01 = Person("P005", "Asa", 20)
    student1 = Student("P001", "Somchai", 20, "S12345")
    staff1 = Staff("P002", "Suda", 35, "ST6789")

    print(student1)
    print(staff1)
    print(person01)

if __name__ == "__main__":
    main()
>>>>>>> 24e134270b137fbb3050eae32f6969ceeb0a14af
