# practical company example
# class variables are attributes that can be accessed by using instances:
# emp_1.raise_amount - first check if instance contains a rise_amount attribute
# and if not check if Employee class or any which inherits from contains that attribute


class Employee:

    num_of_employee = 0
    raise_amount = 1.04  # create a variable

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay

        Employee.num_of_employee += 1  # its Employee var since we don't want it to be different for any instance
        # increments while new instance is created

    def fullname(self):
        return '{} {}'. format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)  # self.raise_amount makes attribute belong to a method


emp_1 = Employee('Jamie', 'Master', 50000)  # emp_1 or any other is a class instance
emp_2 = Employee('Test', 'User', 10000)

# print(emp_1.__dict__)
# print(Employee.__dict__)

print(emp_1.__dict__)  # instance has no raise_amount in its namespace
emp_1.raise_amount = 1.05  # only emp_1 has now a 5% raise instead of 4%
print(emp_1.__dict__)  # instance now has a raise_amount attribute in its namespace

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)  # emp_2 raise_amount attribute still belongs to a class variable

Employee.raise_amount = 1.01  # change class attribute to 1.01
print(Employee.raise_amount)
print(emp_1.raise_amount)  # emp_1 has its own attribute so its not included in Employee class action
print(emp_2.raise_amount)

print("there are {} employees in our company".format(Employee.num_of_employee))
