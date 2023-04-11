
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
        # Alternatively could be accessed using the class itself
        # self.pay = int(self.pay * Employee.raise_amount)

print(Employee.num_of_emp)
emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Test", "User", 60000)
print(Employee.num_of_emp)

# Namespace of class and instance
# print(emp_1.__dict__)
# print(Employee.__dict__)


# Changes the raise amount for the class and all of the instances
# Employee.raise_amount = 1.06


# Only changes the raise amount for the specific instance
# When we make this assignment, it creates the raise_amount within emp_1
emp_1.raise_amount = 1.07

# emp_1 now has raise_amount within it's namespace
# Finds this value in it's own namespace and returns this value before going and searching the class
print(emp_1.__dict__)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)