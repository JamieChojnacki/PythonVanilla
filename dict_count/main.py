vowels = ['a', 'e', 'i', 'o', 'u']
word = input('Provide a word to search for vowels :')

# declare empty dictionary
found = {}

# add objects to dictionary - key and value
found['a'] = 0
found['e'] = 0
found['i'] = 0
found['o'] = 0
found['u'] = 0

for letter in word:
    if letter in vowels:
        found[letter] += 1

for key, value in sorted(found.items()):
    print(key, 'was found', value, 'time(s)')

# you can print value by using a key
print('\n')
print('a was found', found['a'], 'time(s)')
