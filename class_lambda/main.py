class employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({} {} ${})'.format(self.name, self.age, self.salary)


e1 = employee('jakub', 23, 100000)
e2 = employee('marcin', 31, 20000)
e3 = employee('agata', 21, 10000)

# lets sort

employees = [e1, e2, e3]

sorted_emp = sorted(employees, key=lambda sort: sort.name, reverse=True )
print(sorted_emp)
