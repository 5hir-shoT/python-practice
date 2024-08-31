class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}"

student1 = Student("Shirsho", 24, 90.2)
print(student1.get_info())
print(f"Grade: {student1.get_grade()}")



#   Output:
#   Name: Shirsho, Age: 24
#   Grade: 90.2