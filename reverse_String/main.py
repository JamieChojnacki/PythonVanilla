# easy kurwa devSkills challenge from kurwa Accenture made in kurwa python by Jakub Kurwa Chojnacki


class String:

    def __init__(self, string_in, reversed=None):
        """ class constructor """
        self.string_in = string_in
        if reversed is None:  # check if list is empty
            self.reversed = []
        else:
            self.reversed = reversed  # assign to a self object

    def reverse_string(self):
        """ split string and put it in an empty list """
        self.reversed = self.string_in.split()

    def concatenate(self) -> str:
        """ concatenate string and return its final version """
        return " ".join(self.reversed[::-1])

    def __add__(self, other):
        """ lets create a method that adds strings to each other """
        return " ".join(self.reversed[::-1] + other.reversed[::-1])


# get first string
FirstString = String('This is a sample')

# reverse a string and make a new object
FirstString.reverse_string()
first_out = FirstString.concatenate()

# print a final version of string
print(first_out)


""" here comes a bonus second string """


# get second string
SecondString = String('Example from Accenture company job interview')

# reverse a string and make a new object
SecondString.reverse_string()
second_out = SecondString.concatenate()

# print a final version of string
print(second_out)

# TRICK BITCHES
print(FirstString + SecondString)
