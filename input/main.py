vowels = ['a', 'e', 'i', 'u']
word = input("Provide a word to search for vowels : ")              # stdin type
found = []

for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)

for vowel in found:
    print(vowel)