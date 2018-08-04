# create a blue print


class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'. format(self.first, self.last)


emp_1 = Employee('Jamie', 'Chojnacki', 50000)
emp_2 = Employee('Test', 'User', 10000)

print(emp_1.fullname())  # same as Employee.fullname(emp_1)
# print(emp_2)
