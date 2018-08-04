names = ['jakub', 'alicja', 'magda']
names_2 = ['agata', 'agnieszka', 'jagoda']

nums = [1, 2, 3, 4, 5]

names.append('wiktoria')
names.insert(0, 'marcin')

names.extend(names_2)
print(names)

names.reverse()
print(names)

names_2.sort()
print(names_2)

nums.sort(reverse=True)  # sort H-L
print(nums)

sorted_names = sorted(names)  # does not change list
print(sorted_names)

minimal = min(nums)
summand = sum(nums)
print(minimal)
print(summand)

print(names.index('jakub'))  # print index

print()
for index, name in enumerate(names, start=1):  # start 0 -> 1
    print(index, name)

course_str = ' '.join(names_2)
print(course_str)