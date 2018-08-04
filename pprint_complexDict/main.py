import pprint

people ={}

people['kuba'] = {'name': 'Kuba',
                  'home planet': 'earth',
                  'gender': 'male'
                  }
people['maja'] = {'name': 'maja',
                  'home planet': 'titian ala',
                  'gender': 'female'
                  }

print (people['maja']['home planet'])

# pretty print - print in nice eye look
pprint.pprint(people)