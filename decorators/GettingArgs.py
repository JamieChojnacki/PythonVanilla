""" lets make our decorator func invoked with arguments """


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):  # we pass any number of arguments and keyword arguments
        # print('wrapper executed this cell before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function


@decorator_function
def display_info(name, age):
    print('display_info ran with arguments : ({}, {})'.format(name, age))


display_info('Jamie', 21)

