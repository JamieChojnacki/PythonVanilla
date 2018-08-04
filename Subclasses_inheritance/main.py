# inherit instances from a parent class
# create children developer and manager classes


class Employee:  # parent class

    raise_amount = 1.04  # create a parent class variable

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'. format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)  # self.raise_amount makes attribute belong to a method


class Developer(Employee):  # Developer class inherit from Employee class
    raise_amount = 1.30  # developers get better raise

    def __init__(self, first, last, pay, programing_lang):
        super().__init__(first, last, pay)  # let employee class handle those arguments
        # Employee.__init__(self, first, last, pay)  # same as above
        self.programing_lang = programing_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employees(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer('Jamie', 'Master', 50000, 'python')  # we created developer using inherit tool
dev_2 = Developer('Test', 'User', 10000, 'java')  # if __init__ isn't found in children class then search in parent
manager = Manager('Sue', 'Smith', 9000, [dev_1])  # manager supervises developer_1

# print(dev_1.email)
# print(dev_2.email)
# print(help(Developer))  # get info

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

manager.add_employee(dev_2)
print(manager.print_employees())

manager.remove_employee(dev_1)
print(manager.print_employees())

print(isinstance(manager, Manager))  # check if is instance
print(isinstance(manager, Developer))

print(issubclass(Developer, Employee))  # check if is a subclass
