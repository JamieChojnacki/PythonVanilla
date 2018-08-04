def search4letters(phrase: str, letters: str='aeiou') -> set:
    """ return a set of the letters found in phrase"""
    return set(letters).intersection(set(phrase))

import sys

print(sys.path)