def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


def hello(greeting: str, name: str='jakub') -> str:
    return '{}, {}'.format(greeting, name)


print(hello('hi!').upper())

classes = ('math', 'compsci')
sInfo = {'name': 'marcin', 'age': 30}

sInfo.update({'name': 'kuba', 'age': 35})  # update student info

student_info(*classes, **sInfo)
