# __repr__ and __str__ - change how objects are displayed


class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'. format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):  # recreate a object
        return "Employee( '{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        """ add salary """
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('Jamie', 'Master', 90000)
emp_2 = Employee('Test', 'User', 40000)
print(emp_1)

print(repr(emp_1))  # print(emp_1.__repr__())
print(str(emp_1))  # print(emp_1.__str__())

# that how everything works:
print(int.__add__(1, 2))  # same as print(1+2)
print(str.__add__('a', 'b'))  # same as print(a+b)
print('test'.__len__())  # same as print(len('test))

# we created a method that sums employees salary
print(emp_1 + emp_2)
print(len(emp_1))
