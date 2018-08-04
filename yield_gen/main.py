def createGenerator():
    mylist = range(3)
    for i in mylist:
        yield i * i


mygenerator = createGenerator()  # create a generator
print(mygenerator)  # mygenerator is an object!

for i in mygenerator:
    print(i)

# yield is a keyword that is used like return, except the function will return a generator.
