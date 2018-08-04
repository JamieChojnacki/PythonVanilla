# a closure (also lexical closure or function closure) is a technique for implementing lexically scoped name binding
# in a language with first-class functions. Operationally, a closure is a record storing a function
# together with an environment.


# def outer_func():
#     message = 'hi'

    # def inner_func():
    #     print(message)

    # return inner_func


# result = outer_func()
# print(result.__name__)  # check which value is assigned to the object
# result()  # the closure remembers block variables (auto)


""" example 2"""


import logging
logging.basicConfig(filename='example.log', level=logging.INFO)


def logger(func):
    def log_func(*args):  # means we can pass as many args as we want
        logging.info('running "{}" with arguments {}'.format(func.__name__, args))
        print(func(*args))

    return log_func


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


add_logger = logger(add)
sub_logger = logger(sub)
add_logger(3, 3)
sub_logger(20, 10)

