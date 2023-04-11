# class Employee:
#     pass

# Each of these variables are their own unique instances of the Employee class.
# They each contain data that is unique to each instance.

# emp_1 = Employee()  
# emp_2 = Employee()

# Both have different locations in memory.
# <__main__.Employee object at 0x000001FABD84EE00>
# <__main__.Employee object at 0x000001FABD84EE30>


# Instead of manually setting variables which is prone to mistakes, We can use a class method __init__ to setup the variables automatically.


class Employee:
    
    # We can think of this method as initialize
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@email.com"

    # This is a method and needs to be called with parentheses
    def fullname(self):
        return f"{self.first} {self.last}"


emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Test", "User", 60000)

print(emp_1.email)


# emp_2 instance automatically passed to fullname() method
emp_2.fullname()

# Can also run methods on using the class name itself
# When we do this we have to manually pass in the instance as an argument as it doesnt know what instance we want to run the method with
# This is what is going on in the background when we run emp_1.fullname(), it gets transformed into Employee.fullname(emp_1)
Employee.fullname(emp_1)
 