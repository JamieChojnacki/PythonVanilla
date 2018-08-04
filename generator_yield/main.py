def generator(num: int) -> int:
    for n in num:
        yield (n * n)


my_nums = generator([1, 2, 3, 4, 5])
# my_nums = (x*x for x in [1, 2, 3, 4, 5])

for i in my_nums:
    print(i)
