
class Employee:
    
    num_of_emp = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@email.com"

        Employee.num_of_emp += 1

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # repr is meant to be an unambigous representation of the object and should be used for logging and debugging. Meant to be seen by other developers.
    # A good rule of thumb when creating this method is to display something you can copy and paste back into the python code that would recreate that same object
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    # str is meant to be more of a readable representation of an object. Used as a display to the end user.
    def __str__(self):
        return "{} - {}".format(self.fullname(), self.email)

    # Using __add__(), we are telling python how we want to add Employee objects together.
    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())



emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Test", "User", 60000)

# print(emp_1)

# print(repr(emp_1))
# print(str(emp_1))

# print(emp_1.__repr__())
# print(emp_1.__str__())

# print(1 + 2)
# print(int.__add__(1,2))
# print(str.__add__("a", "b"))

# print(emp_1 + emp_2)

# print(len("test"))
# print("test".__len__())

# print(len(emp_1))