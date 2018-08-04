book = "The Hitchhike's guide to the Galaxy"

#list[start:stop:step]

booklist = list(book)
print(booklist[::3])
print(booklist[-6:])
print(booklist[-1:-7:-1])
print(booklist[::-1])

new_phrase = ''.join(booklist[::-1])
print(new_phrase)
