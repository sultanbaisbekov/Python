class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)
    
    def students_birthday(self):
        self.age += 1
    
name = input("Enter student's name: ")
age = int(input("Enter student's age: "))
grades = input('Enter his grades: ')
grades = list(map(int, grades.split()))
student = Student(name, age, grades)

student.students_birthday()

print(f'{student.name} is {student.age} and his average grade is {student.average():.3f}')