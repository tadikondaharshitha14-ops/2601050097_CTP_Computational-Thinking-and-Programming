from dataclasses import dataclass

# Using dataclass
@dataclass
class Student:
    name: str
    age: int
    marks: float

# Traditional class
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

s = Student("Abhi", 20, 85.5)
e = Employee("Anu", 25, 30000)

print("Student:", s)
print("Employee:", e.name, e.age, e.salary)