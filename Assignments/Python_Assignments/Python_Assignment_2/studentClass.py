class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def __str__(self):
        return f"Student Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

student = Student("Alice", 20, "A")
print(student) 