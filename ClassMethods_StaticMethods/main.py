# fresh look on regular methods, class methods and static methods
# regular and class methods take instance as a 1st arg
# regular methods pass self arg, class methods pass cls arg
# static behave as a normal function and don't pass automatically instance args
import datetime


class Employee:

    num_of_employee = 0
    raise_amount = 1.04  # create a class variable

    def __init__(self, first, last, pay):  # self means we work with a instance
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

    @classmethod
    def set_raise_amount(cls, amount):  # we work now with a class not an instance
        cls.raise_amount = amount

    # alternative constructor to work with example 2
    @classmethod
    def from_string(cls, emp_str):  # work with a string which was passed
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)  # same as return Employee(first, last, pay)

    @staticmethod
    def is_work_day(day):
        if day.weekday() == 5 or day.weekday() == 6:  # 0 is monday
            return False
        return True


emp_1 = Employee('Jamie', 'Master', 50000)  # emp_1 or any other is a class instance
emp_2 = Employee('Test', 'User', 10000)

Employee.set_raise_amount(1.05)  # change class variable from 1.04 to 1.05
Employee.raise_amount = 1.05  # same as above
emp_1.raise_amount = 1.04

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)  # emp_2 raise_amount attribute still belongs to a class variable

""" EXAMPLE 2 - class methods works well with separators like hyphens """

emp_str1 = 'John-Doe-70000'
emp_str2 = 'Steve-Smith-30000'
emp_str3 = 'Jane-Doe-90000'

# brutal force :
# first, last, pay = emp_str1.split('-')  # split string and create new objects
# new_emp_1 = Employee(first, last, pay)  # make a new employee and assign to a instance
# print(new_emp_1.email)

# alternative constructor to work with data like these :
emp_3 = Employee.from_string(emp_str1)
print(emp_3.fullname())

my_date = datetime.date.today()
print(Employee.is_work_day(my_date))
