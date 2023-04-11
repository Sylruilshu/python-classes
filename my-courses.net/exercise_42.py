
class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        return f"Name: {self.name} \nAge: {self.age}"

class Student(Person):

    def __init__(self, name, age, section):
        super().__init__(name, age)
        # they have super(),__init__(self, name, age)? the tutorial I watched never included self, reason to/ not to?
        self.section = section

    def display_student(self):
        return f"{super().display()} \nSection: {self.section}"
        # the solution doesnt use super().display(). why not?


person = Person("Bob", "22")
print(person.display())
print("---------------------")
student = Student("foo", "20", "Mathematics")
print(student.display_student())