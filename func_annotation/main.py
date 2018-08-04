def search4vowels(phrase: str) -> set:
    # get string and return set
    vowels = set('aeiou')

    return vowels.intersection(set(phrase))


print('found vowels :', search4vowels('kuba'))
