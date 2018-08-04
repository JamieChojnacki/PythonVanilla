vowels = ['a', 'u', 'i']
word = input('Gimme word :')

found = {}

# method that avoids nonmulti vowels
for letter in word:
    if letter in vowels:
        found.setdefault(letter, 0)
        found[letter] += 1

# lets check the status of our dict
if not found:
    print('dictionary is empty')
else:
    for key, value in sorted(found.items()):
        print(key, 'was found', value, 'time(s)')