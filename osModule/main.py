import os
from datetime import datetime

""" get working directory """
# print(os.getcwd())

""" change directory """
os.chdir('/Users/James/Desktop/')

""" get info about existing files in dir """
# print(os.listdir())

""" make new directory """
# os.mkdir('osDemo')

""" make new directory but with sub directory """
# os.makedirs('osDemo/subDir')

""" remove dir """
# os.rmdr('osDemo')
# os.rmdr('osDemo/some_file')   # remove same_file directory

"""remo demo with sub directory"""
# os.removedirs('osDemo/subDir')

""" rename file """
# os.rename('osDemo.txt', 'some_name.txt')

""" get info """
print(os.stat('ASCII.png'))
# get file size :
print(os.stat('ASCII.png').st_size)

""" get last modification time"""
mod_time = os.stat('ASCII.png').st_atime
print(datetime.fromtimestamp(mod_time))  # readable time format


""" generate tree path (yield) """
# for dirpath, dirnames, filenames in os.walk('/Users/James/Desktop/'):
#     print('current path:', dirpath)
#     print('directories:', dirnames)
#     print('files:', filenames)
#     print()

""" get environment directory """
print(os.environ.get('HOME'))

""" join two directories """
# file_path = os.path.join(os.environ.get('HOME'), 'test.txt')

""" check if path exists """
print(os.path.exists('/tmp/text.txt'))
# os.path.isdir / os.path.isfile - check whether is directory or file

""" split text """
print(os.path.splitext('/temp/temp.txt'))