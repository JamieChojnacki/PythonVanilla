try:
    file = open('currupt.txt')  # if bad name it goes to an exception
    # raise an except manually :
    # if file.name == 'currupt.txt':
    #     raise Exception
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:  # runs if no exception occurs
    file_read = file.read()
    print(file_read)
    file.close()
finally:  # runs no matter what
    print('Executing finally...')
