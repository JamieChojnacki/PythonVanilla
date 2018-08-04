# update name changes and email problems


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property  # property decorator
    def email(self):
        return '{}.{}@company.com'. format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'. format(self.first, self.last)

    @fullname.setter
    def fullname(self, name) :
        """ get new name """
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        """ delete name """
        print('Delete name!')
        self.first = None
        self.last = None


emp_1 = Employee('Jamie', 'Master')
print(emp_1.email)
emp_1.fullname = 'Jamie Chojnacki'
print(emp_1.fullname)

del emp_1.fullname
