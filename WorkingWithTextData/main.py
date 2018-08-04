message = 'lets go!'
secondMessage = 'your welcome'
name = 'kuba'

message.upper()  # to upper
secondMessage.lower()  # to lower

print(len(message))  # strlen
print(message.find('go'))  # search for letter

print(secondMessage.count('o'))  # count letters

new_message = secondMessage.replace('welcome', 'fucked')  # replace string
print(new_message)

greeting = '{}, {}. Welcome!'.format(message, name)  # formating string
fstr_greeting = f'{message}, {name}. Welcome!'  # fstring formating

print(greeting)
print(fstr_greeting)  # they are the same

print(dir(name))  # get info about methodes
print(help(str.lower))  # what does lower method does?
