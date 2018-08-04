""" classes used with decorators """


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):  # we pass any number of arguments and keyword arguments
        return original_function(*args, **kwargs)
    return wrapper_function


class DecoratorClass(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('call method executed this cell before {}'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)


@DecoratorClass
def display_info(name, age):
    print('display_info ran with arguments : ({}, {})'.format(name, age))


@DecoratorClass
def display(arguments):
    value = arguments.pop()
    print(value)


display_info('Jamie', 21)
display([10, 20, 30, 50])
