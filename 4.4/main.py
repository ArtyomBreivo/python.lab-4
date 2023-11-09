#Придумать класс самостоятельно, реализовать в нем методы экземпляра класса,
#статические, методы, методы класса.
class Student:
    students = []

    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major
        Student.students.append(self)

    def study(self, subject):
        print(f"{self.name} изучает {subject}")

    def is_adult(age):
        return age >= 18

    def print_major_info(students):
        print("Информация о специальностях студентов:")
        for student in students:
            print(f"{student.name} учится на специальности {student.major}")

if __name__ == "__main__":
    student1 = Student("Артём", 18, "Информатика")
    student2 = Student("Валерия", 10, "Русский язык")
    student1.study("Программирование")
    student2.study("Лексика")
print(f"{student1.name} является взрослым: {Student.is_adult(student1.age)}")
Student.print_major_info(Student.students)





