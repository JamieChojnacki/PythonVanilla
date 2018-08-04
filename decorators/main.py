# lets work with decorators
# decorator is a func that takes another func as a argument and adds some kind of functionality

""" that's a first class func a closure example """


# def outer_func(msg):
#     def inner_func():
#         print(msg + ' Jamie')
#     return inner_func


# my_func = outer_func('hi')
# my_func()


""" lets jump into decorators """


def decorator_function(original_function):
    def wrapper_function():
        print('wrapper executed this cell before {}'.format(original_function.__name__))
        return original_function()
    return wrapper_function


# def display():
#     print('display function ran')


# decorated_display = decorator_function(display)
# decorated_display()  # execute wrapper function which then executes display func


# prof look:
@decorator_function  # important syntax
def display():
    print('display function ran')


display()

# decorated_display = decorator_function(display)
# decorated_display()
# can be wrapped by using @{func_name} to
# display()

# @decorator_function changes our functionality to
# display = decorator_function(display)
# it means executing display runs decorator_function

