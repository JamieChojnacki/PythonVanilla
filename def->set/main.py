def search4letters(phrase: str, letters: str) -> set:
    return set(phrase).intersection(set(letters))


value = search4letters('lets', 'make it')
print(value)