# lets use decorator with arguments


def prefix_decorator(prefix):
    def decorator_function(original_function):
        def wrapper_function(*args, **kwargs):
            print(prefix, 'executed before', original_function.__name__)
            result = original_function(*args, **kwargs)
            return result
        return wrapper_function
    return decorator_function


class DecoratorClass(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        return self.original_function(*args, **kwargs)


@DecoratorClass
def display_info(name, age):
    print('display_info ran with arguments ({} & {})'.format(name, age))


@prefix_decorator('LOG:')
def display_status(status):
    print('im {} by far'.format(status))


display_status('online')
display_info('jamie', 21)
