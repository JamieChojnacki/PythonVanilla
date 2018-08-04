# Duck Typing and Easier to ask forgiveness than permission (EAFP)


class Duck:

    def quack(self):
        print('Quack, quack')

    def fly(self):
        print('Flap, Flap!')


class Person:

    def quack(self):
        print("I'm Quacking Like a Duck!")

    def fly(self):
        print("I'm Flapping my Arms!")


def quack_and_fly(thing):
    pass
    # Not Duck-Typed (Non-Pythonic)
    # if isinstance(thing, Duck):
    #     thing.quack()
    #     thing.fly()
    # else:
    #     print('This has to be a Duck!')

    # LBYL (Non-Pythonic)
    # if hasattr(thing, 'quack'):
    #     if callable(thing.quack):
    #         thing.quack()

    # if hasattr(thing, 'fly'):
    #     if callable(thing.fly):
    #         thing.fly()

    #     try:
    #         thing.quack()
    #         thing.fly()
    #         thing.bark()
    #     except AttributeError as e:
    #         print(e)

d = Duck()

print(type(dir(d)))

# Pythonic dict usage

person = {'name': 'james', 'age': 21, 'job': 'programmer'}
# KeyError examp :
# person = {'name': 'james', 'age': 21}

try:
    # print("i'm {}. i'm {} years old and i'm a {}.".format(person['name'], person['age'], person['job']))
    print("i'm {name}. i'm {age} years old and i'm a {job}.".format(**person))
except KeyError as e:
    print('missing {} key'.format(e))

