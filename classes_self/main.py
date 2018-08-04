class Person:

    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def introduce(self):
        print('my name is:', self.name)


self_person = Person('kuba', 170, 80)

self_person.introduce()
