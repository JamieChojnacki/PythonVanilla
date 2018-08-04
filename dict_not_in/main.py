fruits = {}

# add key in a run time
if 'apple' not in fruits:
    fruits['apple'] = 0

fruits['apple'] += 1
print(fruits)

#lets use method now
fruits.setdefault('bananas', 0)
fruits['bananas'] += 1
print(fruits)
