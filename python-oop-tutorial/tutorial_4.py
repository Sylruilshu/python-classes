import datetime


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

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod
    def is_work_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

# Parentheses allow us to specify what class we want to inherit from.
class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        # super().__init__ will pass first, last and pay to our Employees init method and let that class handle those arguments.
        super().__init__(first, last, pay)
        # Alternative way
        # Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    # Never want to pass mutible data types like a list or dictionary as default arguments
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        
        # Sets employees to an empty list if the argument is not provided, and set them to that employee list if it is. 
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("--->", emp.fullname())

    # Prints list of Employee objects
    # def print_e(self):
    #     print(self.employees)


dev_1 = Developer("Corey", "Schafer", 50000, "Python")
dev_2 = Developer("Test", "User", 60000, "Java")

mgr_1 = Manager("Sue", "Smith", 90000, [dev_1])

# isinstance will tell us if an object is an instance of a class
# print(isinstance(mgr_1, Manager))
# print(isinstance(mgr_1, Employee))
# print(isinstance(mgr_1, Developer))


# issubclass will tell us if a class is a subclass of another
print(issubclass(Developer, Employee))
print(issubclass(Manager, Employee))
print(issubclass(Developer, Manager))

# why is Developer a subclass of itself???
# print(issubclass(Developer, Developer))
# Prints True

# print(mgr_1.email)

# mgr_1.print_emps()

# print()

# mgr_1.add_emp(dev_2)
# mgr_1.print_emps()

# print()

# mgr_1.remove_emp(dev_1)
# mgr_1.print_emps()

# print(dev_1.email)
# print(dev_1.prog_lang)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

# Shows useful information about method resolution order and inheritance
# print(help(Developer))