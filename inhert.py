#!/usr/bin/python
#Filename:inhert.py

class SchoolMember:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def tell(self):
        print("Name:%s Age:%s" % (self.name, self.age))

class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary=salary
    def tell(self):
        SchoolMember.tell(self)
        print("Salary:%d" % self.salary)

class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks=marks
    def tell(self):
        SchoolMember.tell(self)
        print("marks:%d" % self.marks)

t=Teacher('Mrs.Ssdf', 40, 30000)
s=Student('Swaroop', 22, 75)

members = [t, s]
for member in members:
    member.tell()
