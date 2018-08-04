# In computer science, a programming language is said to have first-class functions if it treats functions as
# first-class citizens. This means the language supports passing functions as arguments to other functions,
# returning them as the values from other functions, and assigning them to variables or storing them in data structures


# first-class citizen (also type, object, entity, or value) in a given programming language is an entity
# which supports all the operations generally available to other entities


""" example 1 """
# assign function to a object variable


def square(x: int) -> int:
    return x * x


# f = square(5)  # parenthesis means we want to execute the function
# f = square  # now we assign a variable to function

# f(5) == f = square(5)
# its available to pass a function as a argument in another function, and return func too

# print(f)
# print(f(5))


""" example 2 """
# use a function inside another function


def my_map(func, arg_list) -> list:
    """ take function from example 1 and a given list """
    result = []
    for i in arg_list:
        result.append(func(i))
    return result


# squares = my_map(square, [1, 2, 3, 4, 5])
# print(squares)


""" example 3 """
# return a function


def logger(msg):
    """ func returns a inner func """

    def log_message():
        print('log:', msg)

    return log_message  # there is no parenthesis - it means the func is not executed


# log_hi = logger('hi')  # log_hi == log_message(returned)
# log_hi()  # execute object variable that was remembered
# that step is called closure !


""" practical example """
# html format


def html_tag(tag):

    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))

    return wrap_text


print_h1 = html_tag('h1')
print_h1('test Headline')
print_h1('another Headline')

print_p = html_tag('p')
print_p('test Paragraph')
